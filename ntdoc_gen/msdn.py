"""MSDN documentation processing."""

import json
import re
from dataclasses import dataclass
from enum import IntEnum, auto
from pathlib import Path
from typing import List, Optional

from .chunk import Chunk, ChunkOrigin
from .ioctl import ctl_code_from_ioctl, get_ioctl_definition


class DocsRepositoryType(IntEnum):
    # With file name prefixes and more-or-less organized structure and metadata.
    ORGANIZED = auto()

    # Without file name prefixes and less organized structure and metadata.
    FUZZY = auto()


@dataclass
class DocsRepositoryInfo:
    title: str
    repository: str
    base_url: str
    base_repository_url: str
    type: DocsRepositoryType


DOCS_REPOSITORY_INFO = {
    ChunkOrigin.MSDN_DDI: DocsRepositoryInfo(
        title='Windows Driver Kit DDI reference',
        repository='windows-driver-docs-ddi',
        base_url='https://learn.microsoft.com/windows-hardware/drivers/ddi/',
        base_repository_url='https://github.com/MicrosoftDocs/windows-driver-docs-ddi/blob/staging/wdk-ddi-src/content/',
        type=DocsRepositoryType.ORGANIZED,
    ),
    ChunkOrigin.MSDN_WIN32: DocsRepositoryInfo(
        title='Win32 API reference',
        repository='sdk-api',
        base_url='https://learn.microsoft.com/windows/win32/api/',
        base_repository_url='https://github.com/MicrosoftDocs/sdk-api/blob/docs/sdk-api-src/content/',
        type=DocsRepositoryType.ORGANIZED,
    ),
    ChunkOrigin.MSDN_DRIVER_FUZZY: DocsRepositoryInfo(
        title='Windows hardware development documentation',
        repository='windows-driver-docs',
        base_url='https://learn.microsoft.com/windows-hardware/drivers/',
        base_repository_url='https://github.com/MicrosoftDocs/windows-driver-docs/blob/staging/windows-driver-docs-pr/',
        type=DocsRepositoryType.FUZZY,
    ),
    ChunkOrigin.MSDN_WIN32_FUZZY: DocsRepositoryInfo(
        title='Win32 development documentation',
        repository='win32',
        base_url='https://learn.microsoft.com/windows/win32/',
        base_repository_url='https://github.com/MicrosoftDocs/win32/blob/docs/desktop-src/',
        type=DocsRepositoryType.FUZZY,
    ),
}


def msdn_docs_header_to_chunk(
    json_path: Path,
    docs_path: Path,
    origin: ChunkOrigin,
    repository_type: DocsRepositoryType,
) -> Optional[Chunk]:
    header_name = ''
    if repository_type == DocsRepositoryType.ORGANIZED:
        header_name = json_path.relative_to(docs_path).parts[0] + '.h'
        header_name = header_name.lower()  # Just to be sure.

    if origin == ChunkOrigin.MSDN_DDI:
        if header_name.lower() in [
            'dbgeng.h',
            'dbgmodel.h',
            'engextcpp.h',
            'portcls.h',
        ]:
            # Contains mostly C++ stuff.
            return None

    with json_path.open('r', encoding='utf-8') as f:
        doc_metadata = json.load(f)

    if repository_type == DocsRepositoryType.FUZZY and '_fuzzy_header' in doc_metadata:
        if header_name:
            assert doc_metadata['_fuzzy_header'] == header_name, json_path
        else:
            header_name = doc_metadata['_fuzzy_header']
            assert isinstance(header_name, str)
            header_name = header_name.lower()  # Just to be sure.

    is_ioctl = False
    if repository_type == DocsRepositoryType.ORGANIZED:
        if json_path.name.startswith('ni-'):
            is_ioctl = True
    elif repository_type == DocsRepositoryType.FUZZY:
        if doc_metadata['_fuzzy_type'] == 'control code':
            is_ioctl = True

    c_path = json_path.with_suffix('.c')
    if not is_ioctl and not c_path.exists():
        return None

    if origin in [ChunkOrigin.MSDN_WIN32, ChunkOrigin.MSDN_WIN32_FUZZY]:
        if is_ioctl or header_name in [
            'winioctl.h',
            'winternl.h',
            'ntddkbd.h',
            'ntdef.h',
        ]:
            # Always include.
            pass
        else:
            is_ntdll_api = False

            req_dll = doc_metadata.get('req.dll') or ''
            if isinstance(req_dll, list):
                if 'ntdll.dll' in [x.lower() for x in req_dll]:
                    is_ntdll_api = True
            else:
                assert isinstance(req_dll, str), json_path
                if re.search(r'\bntdll\.dll\b', req_dll, flags=re.IGNORECASE):
                    is_ntdll_api = True

            if not is_ntdll_api:
                api_location = doc_metadata.get('api_location') or []
                assert isinstance(api_location, list), json_path
                if 'ntdll.dll' in [x.lower() for x in api_location]:
                    is_ntdll_api = True

            if not is_ntdll_api:
                return None

    # Check api_type.
    api_type = doc_metadata.get('api_type')

    if repository_type == DocsRepositoryType.FUZZY:
        if api_type == ['NA']:
            api_type = None
    else:
        assert api_type is not None, json_path

    if api_type is not None:
        assert isinstance(api_type, list), json_path
        assert len(api_type) == 1, json_path
        api_type = api_type[0]

    if api_type in ['COM']:
        return None

    assert api_type is None or api_type in [
        'DllExport',
        'DLLExport',
        'HeaderDef',
        'LibDef',
        'UserDefined',
    ], (json_path, api_type)

    idents = doc_metadata.get('api_name', [])
    assert isinstance(idents, list), json_path

    # Remove duplicates while preserving order.
    idents = list(dict.fromkeys(idents))

    if repository_type == DocsRepositoryType.FUZZY:
        fuzzy_ident = doc_metadata['_fuzzy_ident']
        if idents:
            if fuzzy_ident not in [
                'IOCTL_COPYCHUNK',
                'IOCTL_LMR_DISABLE_LOCAL_BUFFERING',
            ]:
                assert idents == [fuzzy_ident], json_path
        else:
            idents = [fuzzy_ident]

    assert idents, json_path

    if not is_ioctl:
        body = c_path.read_text(encoding='utf-8')

        match = re.search(r'\btypedef\s+(struct|union|enum)\s+(\w+)\s*(?::\s*\w+\s*)?(\S)', body)
        if match:
            assert match.group(3) == '{', json_path
            ident_type = match.group(1)
            ident = match.group(2)
            if not (ident_type == 'struct' and ident == '_NDIS_QOS_SQ_PARAMETERS_ENUM_ARRAY'):
                assert match.start() == 0, json_path
            # Best effort removal of idents which are supposed to have a prefix.
            if ident.startswith('_') or ident.startswith('tag'):
                if ident in idents:
                    idents.remove(ident)
            idents.append(f'{ident_type} {ident}')

        # Move pointer typedefs to the end of the list.
        ident_ptr = [x for x in idents if x.startswith('P') and x[1:] in idents]
        if len(ident_ptr) == 1:
            idents.remove(ident_ptr[0])
            idents.append(ident_ptr[0])
        else:
            assert len(ident_ptr) == 0, json_path

        # Remove A/W variants if the non-suffixed version exists.
        idents = [x for x in idents if not ((x.endswith('A') or x.endswith('W')) and x[:-1] in idents)]

        # Special cases.
        if origin == ChunkOrigin.MSDN_DDI:
            if 'wiauDbgLegacyError2' in idents and 'wiauDbgLegacyError' in idents:
                idents.remove('wiauDbgLegacyError')

            if 'wiauDbgLegacyTrace2' in idents and 'wiauDbgLegacyTrace' in idents:
                idents.remove('wiauDbgLegacyTrace')
        elif origin == ChunkOrigin.MSDN_WIN32:
            if 'ANSI_STRING' in idents:
                idents[idents.index('ANSI_STRING')] = 'STRING'

            # Remove non-Rtl variants if the Rtl one exists.
            idents = [x for x in idents if not f'Rtl{x}' in idents]
    else:
        assert len(idents) == 1, json_path
        ioctl_code = get_ioctl_definition(idents[0])
        if ioctl_code is None:
            body = f'#define {idents[0]} /* IOCTL code */'
        else:
            body = f'// {ctl_code_from_ioctl(ioctl_code)}\n'
            body += f'#define {idents[0]} 0x{ioctl_code:08X}'

    header_name_comment = '// ' + header_name + '\n' if header_name else ''

    code_url = json_path.relative_to(docs_path).with_suffix('').as_posix()

    return Chunk(
        origin=origin,
        code_url=code_url,
        idents=idents,
        before=[(header_name_comment, '')],
        intro='',
        body=body,
        after=[],
    )


def msdn_docs_to_chunks(msdn_docs_path: Path, ids_pattern: Optional[str]) -> List[Chunk]:
    result: List[Chunk] = []

    for chunk_origin, docs_info in DOCS_REPOSITORY_INFO.items():
        docs_path = msdn_docs_path / docs_info.repository
        for json_path in sorted(docs_path.rglob('*.json')):
            if ids_pattern and not re.search(ids_pattern, json_path.stem, flags=re.IGNORECASE):
                continue

            chunk = msdn_docs_header_to_chunk(json_path, docs_path, chunk_origin, docs_info.type)
            if chunk:
                result.append(chunk)

    return result


def is_msdn_chunk_origin(chunk_origin: ChunkOrigin) -> bool:
    return chunk_origin in DOCS_REPOSITORY_INFO.keys()


def get_msdn_doc_url(chunk: Chunk) -> str:
    code_url = chunk.code_url.lower()
    code_url = code_url.replace(',', '_').replace('&', '_').replace('~', '-').replace(' ', '')
    return f'{DOCS_REPOSITORY_INFO[chunk.origin].base_url}{code_url}'


def get_msdn_doc_repository_url(chunk: Chunk) -> str:
    return f'{DOCS_REPOSITORY_INFO[chunk.origin].base_repository_url}{chunk.code_url}.md'


def get_msdn_doc_path(msdn_docs_path: Path, chunk: Chunk) -> Path:
    return msdn_docs_path / DOCS_REPOSITORY_INFO[chunk.origin].repository / (chunk.code_url + '.md')


def get_msdn_origin_title(chunk_origin: ChunkOrigin) -> str:
    return DOCS_REPOSITORY_INFO[chunk_origin].title

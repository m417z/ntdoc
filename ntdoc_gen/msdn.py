"""MSDN documentation processing."""

import json
import re
from pathlib import Path
from typing import List, Optional

from .chunk import Chunk, ChunkOrigin
from .ioctl import ctl_code_from_ioctl, get_ioctl_definition

URL_MSDN_DDI_DOCS = 'https://learn.microsoft.com/windows-hardware/drivers/ddi'
URL_MSDN_DDI_DOCS_REPOSITORY = 'https://github.com/MicrosoftDocs/windows-driver-docs-ddi/blob/staging/wdk-ddi-src/content'

URL_MSDN_WIN32_DOCS = 'https://learn.microsoft.com/windows/win32/api'
URL_MSDN_WIN32_DOCS_REPOSITORY = 'https://github.com/MicrosoftDocs/sdk-api/blob/docs/sdk-api-src/content'


def msdn_docs_header_to_chunk(
    json_path: Path, docs_path: Path, origin: ChunkOrigin
) -> Optional[Chunk]:
    header_name = json_path.relative_to(docs_path).parts[0] + '.h'

    if origin == ChunkOrigin.MSDN_DDI:
        if header_name.lower() in ['dbgeng.h', 'dbgmodel.h', 'portcls.h']:
            # Contains mostly C++ stuff.
            return None

    is_ioctl = json_path.name.startswith('ni-')
    c_path = json_path.with_suffix('.c')
    if not is_ioctl and not c_path.exists():
        return None

    with json_path.open('r', encoding='utf-8') as f:
        doc_metadata = json.load(f)

    if origin == ChunkOrigin.MSDN_WIN32:
        if is_ioctl or header_name.lower() in [
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

    api_type = doc_metadata.get('api_type')
    assert isinstance(api_type, list), json_path
    assert len(api_type) == 1, json_path
    api_type = api_type[0]
    if api_type in ['COM', 'UserDefined']:
        return None
    assert api_type in ['DllExport', 'DLLExport', 'HeaderDef', 'LibDef'], (json_path, api_type)

    idents = doc_metadata.get('api_name', [])
    assert isinstance(idents, list), json_path
    assert idents, json_path

    # Remove duplicates while preserving order.
    idents = list(dict.fromkeys(idents))

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

    header_name_comment = '// ' + header_name + '\n'

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

    doc_sources = [
        ('windows-driver-docs-ddi', ChunkOrigin.MSDN_DDI),
        ('sdk-api', ChunkOrigin.MSDN_WIN32),
    ]

    for docs_subpath, chunk_origin in doc_sources:
        docs_path = msdn_docs_path / docs_subpath
        for json_path in sorted(docs_path.rglob('*.json')):
            if ids_pattern and not re.search(ids_pattern, json_path.stem, flags=re.IGNORECASE):
                continue

            chunk = msdn_docs_header_to_chunk(json_path, docs_path, chunk_origin)
            if chunk:
                result.append(chunk)

    return result


def get_msdn_doc_url(chunk: Chunk) -> str:
    if chunk.origin == ChunkOrigin.MSDN_DDI:
        return f'{URL_MSDN_DDI_DOCS}/{chunk.code_url}'
    if chunk.origin == ChunkOrigin.MSDN_WIN32:
        return f'{URL_MSDN_WIN32_DOCS}/{chunk.code_url}'
    raise RuntimeError(f'Unexpected chunk origin: {chunk.origin}')


def get_msdn_doc_repository_url(chunk: Chunk) -> str:
    if chunk.origin == ChunkOrigin.MSDN_DDI:
        return f'{URL_MSDN_DDI_DOCS_REPOSITORY}/{chunk.code_url}.md'
    if chunk.origin == ChunkOrigin.MSDN_WIN32:
        return f'{URL_MSDN_WIN32_DOCS_REPOSITORY}/{chunk.code_url}.md'
    raise RuntimeError(f'Unexpected chunk origin: {chunk.origin}')


def get_msdn_doc_path(msdn_docs_path: Path, chunk: Chunk) -> Path:
    if chunk.origin == ChunkOrigin.MSDN_DDI:
        return msdn_docs_path / 'windows-driver-docs-ddi' / (chunk.code_url + '.md')
    if chunk.origin == ChunkOrigin.MSDN_WIN32:
        return msdn_docs_path / 'sdk-api' / (chunk.code_url + '.md')
    raise RuntimeError(f'Unexpected chunk origin: {chunk.origin}')


def get_msdn_origin_title(chunk_origin: ChunkOrigin) -> str:
    if chunk_origin == ChunkOrigin.MSDN_DDI:
        return 'Windows Driver Kit DDI reference'
    if chunk_origin == ChunkOrigin.MSDN_WIN32:
        return 'Win32 API reference'
    raise RuntimeError(f'Unexpected chunk origin: {chunk_origin}')

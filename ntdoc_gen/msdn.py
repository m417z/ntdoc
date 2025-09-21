"""MSDN documentation processing."""

import json
import re
from pathlib import Path
from typing import List, Optional

from .chunk import Chunk, ChunkOrigin


def msdn_docs_header_to_chunk(json_path: Path, msdn_docs_path: Path) -> Optional[Chunk]:
    header_name = json_path.relative_to(msdn_docs_path).parts[0] + '.h'
    if header_name.lower() in ['dbgeng.h', 'dbgmodel.h', 'portcls.h']:
        # Contains mostly C++ stuff.
        return None

    c_path = json_path.with_suffix('.c')
    if not c_path.exists():
        return None

    with json_path.open('r', encoding='utf-8') as f:
        doc_metadata = json.load(f)

    if json_path.stem not in [
        'nf-ntifs-selocateprocessimagename',
        'ne-ucmucsispec-_ucsi_usb_operation_role',
        'nf-wdm-keinitializetriagedumpdataarray',
    ]:
        api_type = doc_metadata.get('api_type', None)
        assert isinstance(api_type, list), json_path
        assert len(api_type) == 1, json_path
        api_type = api_type[0]
        if api_type in ['COM', 'UserDefined']:
            return None
        assert api_type in ['DllExport', 'DLLExport', 'HeaderDef', 'LibDef'], (json_path, api_type)

    idents = doc_metadata.get('api_name', [])
    assert isinstance(idents, list), json_path
    assert idents, json_path

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

    if 'wiauDbgLegacyError2' in idents and 'wiauDbgLegacyError' in idents:
        idents.remove('wiauDbgLegacyError')

    if 'wiauDbgLegacyTrace2' in idents and 'wiauDbgLegacyTrace' in idents:
        idents.remove('wiauDbgLegacyTrace')

    header_name_comment = '// ' + header_name + '\n'

    code_url = json_path.relative_to(msdn_docs_path).with_suffix('').as_posix()

    return Chunk(
        origin=ChunkOrigin.MSDN,
        code_url=code_url,
        idents=idents,
        before=[(header_name_comment, '')],
        intro='',
        body=body,
        after=[],
    )


def msdn_docs_to_chunks(msdn_docs_path: Path) -> List[Chunk]:
    result: List[Chunk] = []

    for json_path in sorted(msdn_docs_path.rglob('*.json')):
        chunk = msdn_docs_header_to_chunk(json_path, msdn_docs_path)
        if chunk:
            result.append(chunk)

    return result

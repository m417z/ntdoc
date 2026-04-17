"""Main documentation generation logic."""

from pathlib import Path
from typing import List, Optional

from .chunk import (Chunk, ChunkOrigin, organize_idents_to_ids,
                    remove_redundant_forward_declaration_chunks)
from .html_generator import organize_chunks_to_dir
from .msdn import msdn_docs_to_chunks
from .parser import split_header_to_chunks
from .validator import validate_description_files


def generate_docs(phnt_include_path: Path, msdn_docs_path: Optional[Path], ids_pattern: Optional[str], ntfill_path: Optional[Path] = None):
    chunks: List[Chunk] = []
    for p in sorted(phnt_include_path.glob('*.h')):
        chunks += split_header_to_chunks(p)

    if ntfill_path:
        ntfill_chunks = split_header_to_chunks(ntfill_path, ChunkOrigin.NTFILL)
        header_name_comment = f'// {ntfill_path.name}\n'
        for c in ntfill_chunks:
            c.before.insert(0, (header_name_comment, ''))
        chunks += ntfill_chunks

    if msdn_docs_path:
        chunks += msdn_docs_to_chunks(msdn_docs_path, ids_pattern)

    chunks = remove_redundant_forward_declaration_chunks(chunks)

    ident_to_id = organize_idents_to_ids(chunks)

    assets_path = Path('assets')
    out_path = Path('docs')
    organize_chunks_to_dir(chunks, ident_to_id, assets_path, out_path, ids_pattern, msdn_docs_path)

    validate_description_files()

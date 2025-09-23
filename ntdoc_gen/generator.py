"""Main documentation generation logic."""

from pathlib import Path
from typing import List, Optional

from .chunk import (Chunk, organize_idents_to_ids,
                    remove_redundant_forward_declaration_chunks)
from .html_generator import organize_chunks_to_dir
from .msdn import msdn_docs_to_chunks
from .parser import split_header_to_chunks
from .validator import validate_description_files


def generate_docs(phnt_include_path: Path, msdn_docs_path: Optional[Path], ids_pattern: Optional[str]):
    chunks: List[Chunk] = []
    for p in sorted(phnt_include_path.glob('*.h')):
        chunks += split_header_to_chunks(p)

    if msdn_docs_path:
        chunks += msdn_docs_to_chunks(msdn_docs_path, ids_pattern)

    chunks = remove_redundant_forward_declaration_chunks(chunks)

    ident_to_id = organize_idents_to_ids(chunks)

    assets_path = Path('assets')
    out_path = Path('docs')
    organize_chunks_to_dir(chunks, ident_to_id, assets_path, out_path, ids_pattern)

    validate_description_files()

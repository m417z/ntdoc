"""Description file validation functions."""

import json
from pathlib import Path


def validate_description_files():
    descriptions_ids = set(p.stem for p in Path('descriptions').glob('*.md'))

    with Path('docs', 'ident-to-id.json').open() as f:
        docs_ids = set(json.load(f).values())

    if descriptions_ids != docs_ids:
        print('Warning: Description files and docs do not match.')
        print('To update, run:')
        print()

        non_empty = set()
        empty = set()

        for p in descriptions_ids - docs_ids:
            size = Path('descriptions', p + '.md').stat().st_size
            if size > 0:
                non_empty.add(p)
            else:
                empty.add(p)

        if non_empty:
            print('# Non-empty description files (!!!):')
            for p in sorted(non_empty):
                print(f'rm descriptions/{p}.md')

        if empty:
            print('# Empty description files:')
            for p in sorted(empty):
                print(f'rm descriptions/{p}.md')

        if docs_ids - descriptions_ids:
            print('# Missing description files:')
            for p in sorted(docs_ids - descriptions_ids):
                print(f'touch descriptions/{p}.md')

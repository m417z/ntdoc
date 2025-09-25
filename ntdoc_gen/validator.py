"""Description file validation functions."""

import json
from pathlib import Path


def validate_description_files():
    with Path('docs', 'ident-to-id.json').open() as f:
        docs_ids = set(json.load(f).values())

    description_dirs = [
        Path('descriptions'),
        Path('descriptions', 'undocumented.ntinternals.net'),
    ]

    for description_dir in description_dirs:
        descriptions_ids = set(p.stem for p in description_dir.glob('*.md'))
        if descriptions_ids - docs_ids:
            print('Warning: Description files and docs do not match.')
            print(f'Description dir: {description_dir}')
            print('To update, run:')
            print()

            non_empty = set()
            empty = set()

            for p in descriptions_ids - docs_ids:
                size = (description_dir / (p + '.md')).stat().st_size
                if size > 0:
                    non_empty.add(p)
                else:
                    empty.add(p)

            if non_empty:
                print('# Non-empty description files (!!!):')
                for p in sorted(non_empty):
                    print(f'rm {description_dir / (p + '.md')}')

            if empty:
                print('# Empty description files:')
                for p in sorted(empty):
                    print(f'rm {description_dir / (p + '.md')}')

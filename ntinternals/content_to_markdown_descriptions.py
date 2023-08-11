import json
import re
from pathlib import Path


def text_to_markdown(text: str) -> str:
    # Dot has to be escaped too sometimes, but it's pretty rare to be treated as
    # a special character, and escaping it is too noisy.
    escaped = re.sub(r'([\\`*_{}[\]<>()#+\-!|])', r'\\\1', text)

    # Preserve newlines.
    chunks = escaped.split('\n\n')
    result = []
    for chunk in chunks:
        result.append(re.sub(r'\s*\n', ' \\\n', chunk.strip()))

    return '\n\n'.join(result) + '\n'


def main():
    out_path = Path('../descriptions')
    out_path.mkdir()

    with Path('content.json').open() as f:
        content = json.load(f)

    with Path('phnt-ident-to-id.json').open() as f:
        ident_to_id = json.load(f)

    for ident, item in content.items():
        if ident == 'intro':
            continue

        if ident not in ident_to_id:
            print(f'No id for {ident}')
            continue

        description = item['description'].strip()
        if description == '':
            continue

        description = text_to_markdown(description)

        id = ident_to_id[ident]
        (out_path / f'{id}.md').write_text(description)

    # Create empty files for all the ids that don't have descriptions.
    for id in ident_to_id.values():
        path = out_path / f'{id}.md'
        if not path.exists():
            path.write_text('')


if __name__ == '__main__':
    main()

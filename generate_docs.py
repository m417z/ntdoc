import argparse
import json
import re
import shutil
import time
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Dict, List, Tuple

import markdown2

URL_PHNT_REPOSITORY = 'https://github.com/winsiderss/systeminformer'
URL_DESCRIPTIONS = 'https://github.com/m417z/ntdoc/blob/main/descriptions'
PHNT_REPOSITORY_COMMIT = 'master'  # Updated from command line.

MARKDOWN2_EXTRAS = [
    'cuddled-lists',
    'fenced-code-blocks',
    'header-ids',
    'target-blank-links',
    'tables',
]


def rstrip_line_with_comment(code: str) -> str:
    if '//' in code:
        return code[:code.index('//')].rstrip()
    return code.rstrip()


def pop_next_chunk_custom_marker(code: list) -> str:
    return code.pop(0)


def pop_next_chunk_macro(code: list) -> str:
    macro = code.pop(0)
    while macro.rstrip('\n').endswith('\\'):
        macro += code.pop(0)
    return macro


def pop_next_chunk_struct_union(code: list) -> str:
    line = code.pop(0)
    chunk = line
    if rstrip_line_with_comment(line).endswith(';'):
        return chunk

    assert ';' not in rstrip_line_with_comment(line), line

    while True:
        line = code.pop(0)
        chunk += line
        if line.startswith('}'):
            assert line.rstrip('\n').endswith(';'), line
            break
    return chunk


def starts_with_function_definition(code: list) -> bool:
    # Starts with one of:
    #   FORCEINLINE
    #   _Check_return_ FORCEINLINE
    #   DECLSPEC_NORETURN FORCEINLINE

    if (code[0].startswith('FORCEINLINE') or
        code[0].startswith('_Check_return_ FORCEINLINE') or
        code[0].startswith('DECLSPEC_NORETURN FORCEINLINE')):
        return True

    if (code[0] in ['_Check_return_\n', 'DECLSPEC_NORETURN\n'] and
        code[1].startswith('FORCEINLINE')):
        return True

    return False


def pop_next_chunk_function_definition(code: list) -> str:
    chunk = ''
    while True:
        line = code.pop(0)
        chunk += line
        if line.startswith('}'):
            assert line.rstrip('\n') == '}', line
            break
    return chunk


def pop_next_chunk_default(code: list) -> str:
    chunk = ''
    while True:
        line = code.pop(0)
        chunk += line
        if rstrip_line_with_comment(line).endswith(';'):
            break
        assert ';' not in rstrip_line_with_comment(line), line
    return chunk


def pop_next_chunk(code: list) -> Tuple[str, str, int] | None:
    intro = ''

    while len(code) > 0 and rstrip_line_with_comment(code[0]) == '':
        line = code.pop(0)
        if intro == '' and line.strip() == '':
            continue

        intro += line

    lines_left = len(code)
    if lines_left == 0:
        return None

    assert not code[0].startswith(' '), code[0]

    if code[0].startswith('@'):
        chunk = pop_next_chunk_custom_marker(code)
    elif code[0].startswith('#'):
        chunk = pop_next_chunk_macro(code)
    elif code[0].startswith('typedef struct ') or code[0].startswith('typedef union '):
        chunk = pop_next_chunk_struct_union(code)
    elif starts_with_function_definition(code):
        chunk = pop_next_chunk_function_definition(code)
    else:
        chunk = pop_next_chunk_default(code)

    return intro, chunk, lines_left


def get_chunk_identifiers(chunk: str) -> List[str]:
    if (chunk.startswith('#include') or
        chunk.startswith('#error') or
        chunk.startswith('#undef') or
        chunk.startswith('#define PHNT_') or
        chunk.startswith('C_ASSERT(') or
        chunk.startswith('static_assert(')):
        return []

    # Remove comments and noise, then strip.
    chunk = re.sub(r'\s*//.*$', '', chunk, flags=re.MULTILINE)
    chunk = re.sub(r'^_Function_class_\(\w+\)\s*', '', chunk)
    chunk = chunk.strip()

    if re.match(r'^#define \w+$', chunk):
        return []

    if match := re.match(r'^#define (\w+)[( ]', chunk):
        return [match.group(1)]

    assert not chunk.startswith('#define '), chunk

    if (chunk.startswith('typedef struct') or
        chunk.startswith('typedef union') or
        chunk.startswith('typedef enum')):
        last_index = chunk.rfind('}')
        if last_index != -1:
            assert '{' in chunk, chunk
            idents = chunk[last_index + 1:]
            assert idents.endswith(';'), chunk
            idents = idents.removesuffix(';')

            ident_full = None
            if match := re.match(r'^typedef (struct|union|enum) .*?(\w+)\s*\{', chunk):
                assert not match.group(2).startswith('DECLSPEC'), chunk
                ident_full = match.group(1) + ' ' + match.group(2)
        else:
            # Forward declaration.
            assert '{' not in chunk, chunk
            match = re.match(r'^typedef (struct|union|enum) (\w+)(.*);$', chunk)
            assert match, chunk
            ident_full = match.group(1) + ' ' + match.group(2)
            idents = match.group(3)

        idents = idents.split(',')
        idents = [x.lstrip('* ').rstrip() for x in idents]
        assert len(idents) > 0, chunk
        assert all(re.match(r'^\w+$', x) for x in idents), idents
        return idents + ([ident_full] if ident_full is not None else [])

    # Special cases.
    if chunk == 'typedef _Return_type_success_(return >= 0) LONG NTSTATUS;':
        return ['NTSTATUS']
    if chunk.startswith('typedef NTSTATUS (*PSYSTEM_WATCHDOG_HANDLER)('):
        return ['PSYSTEM_WATCHDOG_HANDLER']
    if chunk.startswith('typedef NTSTATUS ALLOCATE_VIRTUAL_MEMORY_EX_CALLBACK('):
        return ['ALLOCATE_VIRTUAL_MEMORY_EX_CALLBACK']
    if chunk.startswith('typedef NTSTATUS FREE_VIRTUAL_MEMORY_EX_CALLBACK('):
        return ['FREE_VIRTUAL_MEMORY_EX_CALLBACK']
    if chunk.startswith('typedef NTSTATUS QUERY_VIRTUAL_MEMORY_CALLBACK('):
        return ['QUERY_VIRTUAL_MEMORY_CALLBACK']
    if re.match(r'^typedef .*? NTAPI RTL_RUN_ONCE_INIT_FN\(', chunk, flags=re.DOTALL):
        return ['RTL_RUN_ONCE_INIT_FN']
    if re.search(r'^typedef .*? NTAPI WNF_USER_CALLBACK\(', chunk, flags=re.DOTALL | re.MULTILINE):
        return ['WNF_USER_CALLBACK']

    # Example:
    # typedef VOID (NTAPI *PACTIVATION_CONTEXT_NOTIFY_ROUTINE)(...
    if chunk.startswith('typedef ') and (match := re.search(r'\((?:NTAPI|__cdecl|FASTCALL|WINAPI)\s*(?:\*\s*)?(\w+)\)', chunk)):
        return [match.group(1)]

    # Example:
    # typedef PVOID SAM_HANDLE, *PSAM_HANDLE;
    if match := re.match(r'^typedef(?: const)? \w+(?: const)?(?: UNALIGNED)?(.*?)(?:\[.*?\])?;$', chunk):
        idents = match.group(1).split(',')
        idents = [x.lstrip('* ').rstrip() for x in idents]
        assert len(idents) > 0, chunk
        assert all(re.match(r'^\w+$', x) for x in idents), idents
        return idents

    assert not chunk.startswith('typedef '), chunk

    if match := re.search(r'(?:NTAPI|NTAPI_INLINE)\n(\w+)\s*\(', chunk):
        return [match.group(1)]

    assert 'NTAPI' not in chunk, chunk

    if chunk == 'EXTERN_C IMAGE_DOS_HEADER __ImageBase;':
        return ['__ImageBase']

    if match := re.match(r'^DEFINE_GUID\((\w+),', chunk):
        return [match.group(1)]

    if match := re.match(r'^NTSYSAPI \w+ (\w+);$', chunk):
        return [match.group(1)]

    if match := re.match(r'^(?:enum|struct) (\w+);$', chunk):
        return [match.group(1)]

    # Functions.
    if match := re.match(r'^(?:\w+\**\s+)*(\w+)\s*\(', chunk):
        return [match.group(1)]

    assert False, chunk


@dataclass
class Chunk:
    header_name: str
    line_number: int
    idents: List[str]
    before: List[Tuple[str, str]]
    intro: str
    body: str
    after: List[str]


def split_header_to_chunks(path: Path) -> List[Chunk]:
    code = path.read_text()
    original_newline_count = code.count('\n')

    # Tabs to spaces, only at the beginning of the line.
    code = re.sub(r'^\t+', lambda x: 4 * ' ' * len(x.group(0)), code, flags=re.MULTILINE)

    assert '\t' not in code
    assert '@' not in code

    # Remove block comments.
    code = re.sub(r'/\*.*?\*/', lambda x: re.sub(r'[^\n]', '', x.group(0)), code, flags=re.DOTALL)

    # Remove extern "C" declarations.
    code = code.replace('#ifdef __cplusplus\nextern "C" {\n#endif\n', '\n\n\n')
    code = code.replace('#ifdef __cplusplus\n}\n#endif\n', '\n\n\n')

    # Remove other stuff.
    code = code.replace('// Options\n\n//#define PHNT_NO_INLINE_INIT_STRING\n', '\n\n\n')

    # Add custom markers.
    code = re.sub(r'^(// (begin|end)_)', r'@\1', code, flags=re.MULTILINE)

    # Make sure we didn't mess up the line count for line number tracking.
    assert code.count('\n') == original_newline_count

    code = code.splitlines(keepends=True)
    code_lines_total = len(code)

    chunks = []
    while True:
        next_chunk = pop_next_chunk(code)
        if next_chunk is None:
            break

        intro, body, lines_left = next_chunk
        line_number = code_lines_total - lines_left + 1

        chunks.append((intro, body, line_number))

    result: List[Chunk] = []

    before = []
    after = []
    for intro, body, line_number in chunks:
        if body.startswith('#if'):
            before.append((intro, body))
            after.insert(0, '#endif\n')
            continue

        if body.startswith('@// begin_'):
            before.append((intro, body[1:]))
            after.insert(0, re.sub(r'^@// begin_(\w+).*$', r'// end_\1', body))
            continue

        if body.startswith('#endif'):
            _, popped_before = before.pop()
            popped_after = after.pop(0)
            assert popped_before.startswith('#if'), popped_before
            assert popped_after.startswith('#endif'), popped_after
            continue

        if body.startswith('@// end_'):
            _, popped_before = before.pop()
            popped_after = after.pop(0)
            assert popped_before.startswith('// begin_'), popped_before
            assert popped_after.startswith('// end_'), popped_after
            continue

        if body.startswith('#else'):
            popped_before_intro, popped_before = before.pop()
            assert popped_before.startswith('#if'), popped_before
            before.append((popped_before_intro, popped_before + '// ...\n' + body))
            continue

        if body.startswith('#elif '):
            popped_before_intro, popped_before = before.pop()
            assert popped_before.startswith('#if '), popped_before
            before.append((intro, popped_before + '// ...\n' + body))
            continue

        idents = get_chunk_identifiers(body)
        if len(idents) == 0:
            continue

        result.append(Chunk(path.name, line_number, idents, before.copy(), intro, body, after.copy()))

    return result


def remove_redundant_forward_declaration_chunks(chunks: List[Chunk]) -> List[Chunk]:
    result: List[Chunk] = []

    for chunk in chunks:
        if re.match(r'^(typedef )?(struct|union|enum) (\w+).*;(\s*//.*)?$', chunk.body):
            idents_unique = set(chunk.idents)

            for chunk_other in chunks:
                if chunk_other is chunk:
                    continue

                for ident in list(idents_unique):
                    if ident in chunk_other.idents:
                        idents_unique.remove(ident)

            if idents_unique == set():
                continue

        result.append(chunk)

    return result


def organize_idents_to_ids(chunks: List[Chunk]):
    ident_to_id: Dict[str, str] = {}
    id_update_from_to_collisions: Dict[str, str] = {
        # Collides with function WinStationShadow.
        'WINSTATIONSHADOW': 'struct-winstationshadow',
    }
    id_update_from_to = id_update_from_to_collisions.copy()

    for chunk in chunks:
        id = chunk.idents[0]
        for ident in chunk.idents:
            if ident not in ident_to_id:
                ident_to_id[ident] = id
            elif 'P' + ident_to_id[ident] == id:
                id_update_from_to['P' + ident_to_id[ident]] = ident_to_id[ident]
            elif ident_to_id[ident] == 'P' + id:
                id_update_from_to['P' + id] = id
            elif {ident_to_id[ident], id} == {'FSINFOCLASS', 'FS_INFORMATION_CLASS'}:
                # Special case.
                id_update_from_to['FSINFOCLASS'] = 'FS_INFORMATION_CLASS'
            else:
                assert ident_to_id[ident] == id, (ident, ident_to_id[ident], id)

    # ZwAbc and NtAbc are the same, assign the same id.
    for k in ident_to_id:
        if k.startswith('Zw'):
            nt_k = 'Nt' + k[2:]
            assert nt_k in ident_to_id, (k, nt_k)
            ident_to_id[k] = ident_to_id[nt_k]

    for k in ident_to_id:
        if ident_to_id[k] in id_update_from_to:
            ident_to_id[k] = id_update_from_to[ident_to_id[k]]

    id_lower_case_mapping = {}
    for k in ident_to_id:
        id_lower_case = ident_to_id[k].lower()
        id_original_case = ident_to_id[k]

        if id_lower_case in id_lower_case_mapping:
            assert id_lower_case_mapping[id_lower_case] == id_original_case, (
                f'Different case for {id_original_case}: {id_lower_case_mapping[id_lower_case]} vs {id_original_case}')
        else:
            id_lower_case_mapping[id_lower_case] = id_original_case

        ident_to_id[k] = id_lower_case
        assert re.match(r'^[a-z0-9_]+$', ident_to_id[k]) or ident_to_id[k] in id_update_from_to_collisions.values(), ident_to_id[k]

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        for ident in chunk.idents[1:]:
            assert ident_to_id[ident] == id, (ident, ident_to_id[ident], id)

    return ident_to_id


def chunk_to_html(chunk: Chunk) -> str:
    header_name = chunk.header_name
    line_number = chunk.line_number
    before = chunk.before
    intro = chunk.intro
    body = chunk.body
    after = chunk.after

    html_before = ''
    for x, y in before:
        html_before += escape(f'{x}{y}')

    # Remove empty lines.
    html_before = re.sub(r'\n\n+', '\n', html_before)

    html_before += '\n'

    html_after = ''
    for x in after:
        html_after += escape(x)

    # Remove empty lines.
    html_after = re.sub(r'\n\n+', '\n', html_after)

    html_after = '\n' + html_after

    code_url = URL_PHNT_REPOSITORY + f'/blob/{PHNT_REPOSITORY_COMMIT}/phnt/include/{header_name}#L{line_number}'

    html = '<pre class="ntdoc-code-pre">'
    html += '<code class="ntdoc-code">'
    html += '<span class="ntdoc-code-header">'
    html += html_before
    html += '</span>'
    html += '<span class="ntdoc-code-intro">'
    html += escape(intro)
    html += '</span>'
    html += '<span class="ntdoc-code-body">'
    html += escape(body)
    html += '</span>'
    html += '<span class="ntdoc-code-footer">'
    html += html_after
    html += '</span>'
    html += '<span class="ntdoc-code-links">'
    html += '<hr>'
    html += f'<a target="_blank" href="{code_url}">View code on GitHub</a>'
    html += '</span>'
    html += '</code>'
    html += '</pre>'

    return html


def html_add_id_links(html: str, ident_to_id: Dict[str, str], exclude_id: str | None, id_to_body: Dict[str, str]) -> str:
    # Sort by length to avoid matching substrings, e.g. "struct ABC" should
    # match before "ABC".
    ids_sorted_by_length = sorted(ident_to_id.keys(), key=lambda x: len(x), reverse=True)

    regex = rf'\b({"|".join(ids_sorted_by_length)})\b'

    def repl(match):
        ident = match.group(1)
        id = ident_to_id[ident]
        if id == exclude_id:
            return ident

        tooltip_text = id_to_body[id].strip()

        tooltip_text_lines_max = 20
        tooltip_text_lines = tooltip_text.splitlines()
        if len(tooltip_text_lines) > tooltip_text_lines_max:
            tooltip_text = '\n'.join(tooltip_text_lines[:tooltip_text_lines_max]) + '\n...'
        elif len(tooltip_text_lines) == 1:
            # Remove extra whitespace in defines such as:
            # #define FILE_CREATED                    0x00000002
            tooltip_text = re.sub(r'^(#define \w+ )\s+', r'\1', tooltip_text)

        tooltip_text_escaped = escape(tooltip_text).replace('\n', '&#10;')

        return f'<a href="{id}" title="{tooltip_text_escaped}">{ident}</a>'

    return re.sub(regex, repl, html)


def changelog_to_html(ident_to_id: Dict[str, str], id_to_body: Dict[str, str]) -> Tuple[str, str]:
    changelog_path = Path('CHANGELOG.md')
    changelog = changelog_path.read_text()

    changelog_markdown = changelog.split('<!-- content -->', 1)[1].lstrip()
    changelog_markdown_short = changelog_markdown.split('<!-- more -->', 1)[0]

    changelog_short = '<div class="ntdoc-changelog-short">\n'
    changelog_short += '<h1>Recent content changes</h1>\n'
    changelog_short += markdown2.markdown(changelog_markdown_short, extras=MARKDOWN2_EXTRAS)
    changelog_short += '<a href="changelog">All content changes</a>\n'
    changelog_short += '</div>\n'

    # h2 -> h3, h1 -> h2.
    changelog_short = re.sub(r'(</?h)2\b', r'\g<1>3', changelog_short)
    changelog_short = re.sub(r'(</?h)1\b', r'\g<1>2', changelog_short)

    changelog_full = '<div class="ntdoc-description ntdoc-changelog-full">\n'
    changelog_full += markdown2.markdown(changelog_markdown, extras=MARKDOWN2_EXTRAS)
    changelog_full += '</div>\n'

    changelog_full = html_add_id_links(changelog_full, ident_to_id, None, id_to_body)

    return changelog_short, changelog_full


def organize_chunks_to_dir(chunks: List[Chunk], ident_to_id: Dict[str, str], assets_path: Path, out_path: Path, ids_pattern: str | None):
    shutil.copytree(assets_path, out_path)

    html_page_template_path = out_path / 'page-template.html'
    html_page_template = html_page_template_path.read_text()
    html_page_template_path.unlink()

    id_to_html_contents: Dict[str, List[str]] = {}
    id_to_id_human: Dict[str, str] = {}
    id_to_body: Dict[str, str] = {}

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        html = chunk_to_html(chunk)
        id_to_html_contents.setdefault(id, []).append(html)

        id_parts = id.split('-')
        assert 1 <= len(id_parts) <= 2, id
        id_to_match = id_parts[-1]

        id_human_candidates = [x for x in chunk.idents if x.lower() == id_to_match.lower()]
        assert len(id_human_candidates) <= 1, (id, chunk.idents)

        if len(id_human_candidates) > 0:
            assert id not in id_to_id_human or id_to_id_human[id] == id_human_candidates[0]
            id_to_id_human[id] = id_human_candidates[0]

        if id not in id_to_body:
            id_to_body[id] = chunk.body

    for id, html_contents in id_to_html_contents.items():
        if ids_pattern and not re.search(ids_pattern, id, flags=re.IGNORECASE):
            continue

        html = '<div class="ntdoc-code-elements">\n'

        for html_content in html_contents:
            html += '<div class="ntdoc-code-element">\n'
            html += html_add_id_links(html_content, ident_to_id, id, id_to_body)
            html += '</div>\n'

        html += '</div>\n'

        html += '<div class="ntdoc-description">\n'

        description_path = Path('descriptions', f'{id}.md')
        description = description_path.read_text().strip() if description_path.exists() else ''
        if description != '':
            # GitHub markdown supports newline with trailing "\", but markdown2
            # only supports trailing "  ".
            # https://github.com/trentm/python-markdown2/issues/525
            description = re.sub(r'\\\n', '  \n', description)

            html_description = markdown2.markdown(description, extras=MARKDOWN2_EXTRAS)

            html += html_add_id_links(html_description, ident_to_id, id, id_to_body)
        else:
            html += '<div class="ntdoc-description-none">\n'
            html += '<p>No description available.</p>\n'
            html += '</div>\n'

        html += '</div>\n'
        html += '<div class="ntdoc-description-links">\n'
        html += f'<a target="_blank" href="{URL_DESCRIPTIONS}/{id}.md">Edit description on GitHub</a>\n'
        html += '</div>\n'

        html_page = html_page_template.replace('{{id}}', id_to_id_human[id]).replace('{{content}}', html)
        (out_path / f'{id}.html').write_text(html_page)

    with (out_path / 'ident-to-id.json').open('w') as f:
        json.dump(ident_to_id, f, indent=0, sort_keys=True)

    html = ''
    for ident in sorted(ident_to_id):
        html += f'<div><a href="{ident_to_id[ident]}">{ident}</a></div>\n'

    html_page = html_page_template.replace('{{id}}', 'Symbols').replace('{{content}}', html)
    (out_path / f'symbols.html').write_text(html_page)

    changelog_short, changelog_full = changelog_to_html(ident_to_id, id_to_body)

    index_html_path = out_path / 'index.html'
    index_html_path.write_text(index_html_path.read_text().replace('{{changelog}}', changelog_short))

    html_page = html_page_template.replace('{{id}}', 'Content changes').replace('{{content}}', changelog_full)
    (out_path / f'changelog.html').write_text(html_page)


def generate_docs(phnt_include_path: Path, ids_pattern: str | None):
    chunks: List[Chunk] = []
    for p in sorted(phnt_include_path.glob('*.h')):
        chunks += split_header_to_chunks(p)

    chunks = remove_redundant_forward_declaration_chunks(chunks)

    ident_to_id = organize_idents_to_ids(chunks)

    assets_path = Path('assets')
    out_path = Path('docs')
    organize_chunks_to_dir(chunks, ident_to_id, assets_path, out_path, ids_pattern)


def validate_description_files():
    descriptions_ids = set(p.stem for p in Path('descriptions').glob('*.md'))

    with Path('docs', 'ident-to-id.json').open() as f:
        docs_ids = set(json.load(f).values())

    if descriptions_ids != docs_ids:
        print('Warning: Description files and docs do not match.')
        print('To update, run:')
        print()

        for p in sorted(descriptions_ids - docs_ids):
            size = Path('descriptions', p + '.md').stat().st_size
            print(f'rm descriptions/{p}.md # size={size}')

        for p in sorted(docs_ids - descriptions_ids):
            print(f'touch descriptions/{p}.md')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="phnt include path", required=True)
    parser.add_argument("-c", "--commit", help="phnt commit")
    parser.add_argument("-i", "--ids-pattern",
                        help="generate only the ids matching the regex pattern, "
                             "useful for testing to quickly generate a subset of the docs")
    args = parser.parse_args()

    phnt_include_path = Path(args.path)

    global PHNT_REPOSITORY_COMMIT
    if args.commit is not None:
        PHNT_REPOSITORY_COMMIT = args.commit

    start = time.time()

    generate_docs(phnt_include_path, args.ids_pattern)
    validate_description_files()

    end = time.time()
    print(f'Finished in {end - start:.2f}s')


if __name__ == '__main__':
    main()

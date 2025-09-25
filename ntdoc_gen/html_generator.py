"""HTML generation and templating functions."""

import json
import re
import shutil
from collections import defaultdict
from html import escape
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import config
from .chunk import Chunk, ChunkOrigin
from .markdown import markdown_to_html
from .msdn import (get_msdn_doc_path, get_msdn_doc_repository_url,
                   get_msdn_doc_url, get_msdn_origin_title)


def chunk_to_html(chunk: Chunk) -> str:
    origin = chunk.origin
    code_url = chunk.code_url
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

    code_full_url = code_url
    code_link_title = 'View code'
    if origin == ChunkOrigin.PHNT:
        code_full_url = config.URL_PHNT_REPOSITORY + f'/blob/{config.PHNT_REPOSITORY_COMMIT}/phnt/include/' + code_url
        code_link_title = 'View code on GitHub'
    elif origin in [ChunkOrigin.MSDN_DDI, ChunkOrigin.MSDN_WIN32]:
        code_full_url = get_msdn_doc_url(chunk)
        code_link_title = f'View the official {get_msdn_origin_title(chunk.origin)}'

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
    html += f'<a target="_blank" href="{code_full_url}">{escape(code_link_title)}</a>'
    html += '</span>'
    html += '</code>'
    html += '</pre>'

    return html


def html_add_id_links(
    html: str,
    ident_to_id: Dict[str, str],
    exclude_id: Optional[str],
    id_to_tooltip_text: Dict[str, str],
) -> str:
    # Sort by length to avoid matching substrings, e.g. "struct ABC" should
    # match before "ABC".
    ids_sorted_by_length = sorted(ident_to_id.keys(), key=lambda x: len(x), reverse=True)

    regex = rf'\b({"|".join(ids_sorted_by_length)})\b'

    def repl(match):
        start_index = match.start()
        a_open_count = html.count('<a', 0, start_index)
        a_end_count = html.count('</a>', 0, start_index)
        if a_open_count > a_end_count:
            # Already inside a link, skip.
            return match.group(0)

        ident = match.group(1)
        id = ident_to_id[ident]
        if id == exclude_id:
            return ident

        tooltip_text = id_to_tooltip_text[id].strip()

        tooltip_text_lines_max = 20
        tooltip_text_lines = tooltip_text.splitlines()
        if len(tooltip_text_lines) > tooltip_text_lines_max:
            tooltip_text = '\n'.join(tooltip_text_lines[:tooltip_text_lines_max]) + '\n...'
        elif len(tooltip_text_lines) == 1:
            # Remove extra whitespace in lines such as:
            # #define FILE_CREATED                    0x00000002
            # typedef long                LONG;
            if tooltip_text.startswith('#define ') or tooltip_text.startswith('typedef '):
                tooltip_text = re.sub(r'\s+', ' ', tooltip_text)

        tooltip_text_escaped = escape(tooltip_text).replace('\n', '&#10;')

        return f'<a href="{id}" title="{tooltip_text_escaped}">{ident}</a>'

    return re.sub(regex, repl, html)


def validate_chunks_amount(id: str, chunks: List[Chunk]):
    chunks_per_origin = defaultdict(int)
    for chunk in chunks:
        chunks_per_origin[chunk.origin] += 1

    known_high_amounts = {
        # phnt.
        ('c_assert', ChunkOrigin.PHNT): 4,
        ('context_ex_padding', ChunkOrigin.PHNT): 4,
        ('context_frame_length', ChunkOrigin.PHNT): 4,
        ('mofresourceinfo', ChunkOrigin.PHNT): 4,
        ('size_t_max', ChunkOrigin.PHNT): 4,
        ('size_t', ChunkOrigin.PHNT): 4,
        # msdn.
        ('barrierafterread', ChunkOrigin.MSDN_DDI): 6,
        ('field_offset', ChunkOrigin.MSDN_DDI): 5,
        ('read_port_uchar', ChunkOrigin.MSDN_DDI): 4,
        ('read_port_ulong', ChunkOrigin.MSDN_DDI): 4,
        ('read_port_ushort', ChunkOrigin.MSDN_DDI): 4,
        ('read_register_uchar', ChunkOrigin.MSDN_DDI): 4,
        ('read_register_ulong', ChunkOrigin.MSDN_DDI): 4,
        ('read_register_ushort', ChunkOrigin.MSDN_DDI): 4,
        ('rtlzeromemory', ChunkOrigin.MSDN_DDI): 6,
        ('write_port_uchar', ChunkOrigin.MSDN_DDI): 4,
        ('write_port_ulong', ChunkOrigin.MSDN_DDI): 4,
        ('write_port_ushort', ChunkOrigin.MSDN_DDI): 4,
        ('write_register_uchar', ChunkOrigin.MSDN_DDI): 4,
        ('write_register_ulong', ChunkOrigin.MSDN_DDI): 4,
        ('write_register_ushort', ChunkOrigin.MSDN_DDI): 4,
    }

    max_origin, max_origin_count = max(chunks_per_origin.items(), key=lambda x: x[1])
    max_origin_count_threshold = known_high_amounts.get((id, max_origin), 3)
    if max_origin_count > max_origin_count_threshold:
        print(f'Warning: Many elements for {id}: {max_origin_count} from {max_origin.name}')


def get_code_elements_html(
    chunks: List[Chunk],
    ident_to_id: Dict[str, str],
    id: str,
    id_to_body: Dict[str, str],
) -> str:
    html = '<div class="ntdoc-code-elements">\n'

    for chunk in chunks:
        html_content = chunk_to_html(chunk)
        html += '<div class="ntdoc-code-element">\n'
        html += html_add_id_links(html_content, ident_to_id, id, id_to_body)
        html += '</div>\n'

    html += '</div>\n'
    return html


def get_ntdoc_description_markdown(id: str) -> Tuple[str, bool]:
    description_path = Path('descriptions', f'{id}.md')
    description = description_path.read_text().strip() if description_path.exists() else ''

    prefer_over_fallback = True

    if description:
        # Check if the description is just a link to an external documentation.
        if description.startswith('This ') and 'documented in' in description:
            description_stripped = description.strip()
            if not '\n' in description_stripped:
                # Remove links.
                description_stripped = re.sub(r'\(https?://.*?\)', '', description_stripped)
                if description_stripped.endswith('.') and '.' not in description_stripped[:-1]:
                    prefer_over_fallback = False
    else:
        prefer_over_fallback = False

    return description, prefer_over_fallback


def get_ntdoc_description_html(
    markdown: str,
    is_selected: bool,
    id: str,
    ident_to_id: Dict[str, str],
    id_to_body: Dict[str, str],
) -> str:
    if markdown:
        html_description = markdown_to_html(markdown, header_ids=is_selected)
        html = html_add_id_links(html_description, ident_to_id, id, id_to_body)
    else:
        html = '<div class="ntdoc-description-none">\n'
        html += '<p>No description available.</p>\n'
        html += '</div>\n'

    html += '<div class="ntdoc-description-links">\n'
    html += f'<a target="_blank" href="{config.URL_DESCRIPTIONS}/{id}.md">Edit description on GitHub</a>\n'
    html += '</div>\n'

    return html


def get_ntinternals_description_html(
    is_selected: bool, id: str, ident_to_id: Dict[str, str], id_to_body: Dict[str, str]
) -> Optional[str]:
    description_path = Path('descriptions', 'undocumented.ntinternals.net', f'{id}.md')
    description = description_path.read_text().strip() if description_path.exists() else ''
    if description == '':
        return None

    html_description = markdown_to_html(description, header_ids=is_selected)
    html = html_add_id_links(html_description, ident_to_id, id, id_to_body)

    html += '<div class="ntdoc-description-links">\n'
    html += f'<a target="_blank" href="{config.URL_DESCRIPTIONS}/undocumented.ntinternals.net/{id}.md">Edit description on GitHub</a>\n'
    html += '</div>\n'

    return html


def get_msdn_description_html(
    chunk: Chunk,
    is_selected: bool,
    id: str,
    ident_to_id: Dict[str, str],
    id_to_body: Dict[str, str],
    msdn_docs_path: Path,
) -> str:
    description_path = get_msdn_doc_path(msdn_docs_path, chunk)
    description = description_path.read_text().strip() if description_path.exists() else ''
    if description == '':
        raise RuntimeError(f'MSDN description not found: {description_path}')

    html_description = markdown_to_html(description, header_ids=is_selected)
    html = html_add_id_links(html_description, ident_to_id, id, id_to_body)

    code_full_url = get_msdn_doc_url(chunk)
    code_link_title = f'View the official {get_msdn_origin_title(chunk.origin)}'

    html += '<hr>\n'
    html += '<div class="ntdoc-description-links">\n'
    html += '<p>\n'
    html += f'<a target="_blank" href="{code_full_url}">{escape(code_link_title)}</a>\n'
    html += '</p>\n'
    html += f'<a target="_blank" href="{get_msdn_doc_repository_url(chunk)}">Edit description on GitHub</a>\n'
    html += '</div>\n'

    return html


def get_descriptions_html(
    chunks: List[Chunk],
    ident_to_id: Dict[str, str],
    id: str,
    id_to_body: Dict[str, str],
    msdn_docs_path: Optional[Path],
) -> str:
    html = '<div class="ntdoc-descriptions">\n'

    markdown_ntdoc, prefer_ntdoc_over_fallback = get_ntdoc_description_markdown(id)

    descriptions: List[Tuple[str, str]] = []

    for chunk in chunks:
        if chunk.origin in [ChunkOrigin.MSDN_DDI, ChunkOrigin.MSDN_WIN32] and msdn_docs_path:
            is_selected = not prefer_ntdoc_over_fallback and len(descriptions) == 0
            description_msdn = get_msdn_description_html(
                chunk, is_selected, id, ident_to_id, id_to_body, msdn_docs_path
            )
            title_msdn = f'{get_msdn_origin_title(chunk.origin)} ({chunk.code_url.split("/")[-1]})'
            descriptions.append((title_msdn, description_msdn))

    is_selected = not prefer_ntdoc_over_fallback and len(descriptions) == 0
    description_ntinternals = get_ntinternals_description_html(
        is_selected, id, ident_to_id, id_to_body
    )
    if description_ntinternals:
        title_ntinternals = 'NTinternals.net (undocumented.ntinternals.net)'
        descriptions.append((title_ntinternals, description_ntinternals))

    selected_index = 0
    if not prefer_ntdoc_over_fallback and len(descriptions) > 0:
        selected_index = 1

    description_ntdoc = get_ntdoc_description_html(
        markdown_ntdoc, selected_index == 0, id, ident_to_id, id_to_body
    )
    descriptions.insert(0, ('NtDoc', description_ntdoc))

    for i, (title, description) in enumerate(descriptions):
        html += '<div class="ntdoc-description-title">\n'
        html += f'<h1>{escape(title)}</h1>\n'
        html += '</div>\n'

        ntdoc_description_class = 'ntdoc-description'
        if i == selected_index:
            ntdoc_description_class += ' ntdoc-description-selected'

        html += f'<div class="{ntdoc_description_class}">\n'
        html += description
        html += '</div>\n'

    html += '</div>\n'
    return html


def changelog_to_html(ident_to_id: Dict[str, str], id_to_tooltip_text: Dict[str, str]) -> Tuple[str, str]:
    changelog_path = Path('CHANGELOG.md')
    changelog = changelog_path.read_text()

    changelog_markdown = changelog.split('<!-- content -->', 1)[1].lstrip()
    changelog_markdown_short = changelog_markdown.split('<!-- more -->', 1)[0]

    changelog_short = '<div class="ntdoc-changelog-short">\n'
    changelog_short += '<h1>Recent content changes</h1>\n'
    changelog_short += markdown_to_html(changelog_markdown_short)
    changelog_short += '<a href="changelog">All content changes</a>\n'
    changelog_short += '</div>\n'

    # h2 -> h3, h1 -> h2.
    changelog_short = re.sub(r'(</?h)2\b', r'\g<1>3', changelog_short)
    changelog_short = re.sub(r'(</?h)1\b', r'\g<1>2', changelog_short)

    changelog_full = '<div class="ntdoc-description ntdoc-changelog-full">\n'
    changelog_full += markdown_to_html(changelog_markdown)
    changelog_full += '</div>\n'

    changelog_full = html_add_id_links(changelog_full, ident_to_id, None, id_to_tooltip_text)

    return changelog_short, changelog_full


def organize_chunks_to_dir(
    chunks: List[Chunk],
    ident_to_id: Dict[str, str],
    assets_path: Path,
    out_path: Path,
    ids_pattern: Optional[str],
    msdn_docs_path: Optional[Path],
):
    shutil.copytree(assets_path, out_path)

    html_page_template_path = out_path / 'page-template.html'
    html_page_template = html_page_template_path.read_text()
    html_page_template_path.unlink()

    id_to_chunks: Dict[str, List[Chunk]] = {}
    id_to_id_human: Dict[str, str] = {}
    id_to_tooltip_text: Dict[str, str] = {}

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        id_to_chunks.setdefault(id, []).append(chunk)

        id_parts = id.split('-')
        if len(id_parts) == 1:
            id_to_match = id_parts[0]
        else:
            assert len(id_parts) == 2, id
            if id_parts[1].rstrip('0123456789'):
                assert id_parts[1] in ['struct', 'union', 'enum'], id_parts
                id_to_match = id_parts[1] + ' ' + id_parts[0]
            else:
                id_to_match = id_parts[0]

        id_human_candidates = [x for x in chunk.idents if x.lower() == id_to_match.lower()]
        assert len(id_human_candidates) <= 1, (id, chunk.idents)

        if len(id_human_candidates) > 0:
            assert id not in id_to_id_human or id_to_id_human[id] == id_human_candidates[0]
            id_to_id_human[id] = id_human_candidates[0]

        if id not in id_to_tooltip_text:
            id_to_tooltip_text[id] = chunk.body

    for id, chunks in id_to_chunks.items():
        # Warn if there are too many chunks for a single id. This may indicate a
        # bug which assigns the same id to multiple unrelated chunks.
        validate_chunks_amount(id, chunks)

        if ids_pattern and not re.search(ids_pattern, id, flags=re.IGNORECASE):
            continue

        html = get_code_elements_html(chunks, ident_to_id, id, id_to_tooltip_text)
        html += get_descriptions_html(chunks, ident_to_id, id, id_to_tooltip_text, msdn_docs_path)

        html_page = html_page_template.replace('{{id}}', id_to_id_human[id]).replace('{{content}}', html)
        (out_path / f'{id}.html').write_text(html_page)

    with (out_path / 'ident-to-id.json').open('w') as f:
        json.dump(ident_to_id, f, indent=0, sort_keys=True)

    html = ''
    for ident in sorted(ident_to_id):
        html += f'<div><a href="{ident_to_id[ident]}">{ident}</a></div>\n'

    html_page = html_page_template.replace('{{id}}', 'Symbols').replace('{{content}}', html)
    (out_path / f'symbols.html').write_text(html_page)

    changelog_short, changelog_full = changelog_to_html(ident_to_id, id_to_tooltip_text)

    index_html_path = out_path / 'index.html'
    index_html_path.write_text(index_html_path.read_text().replace('{{changelog}}', changelog_short))

    html_page = html_page_template.replace('{{id}}', 'Content changes').replace('{{content}}', changelog_full)
    (out_path / f'changelog.html').write_text(html_page)

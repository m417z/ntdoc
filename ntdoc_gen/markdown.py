"""Markdown processing utilities."""

import re

import markdown2


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
    extras = {
        'breaks': {'on_backslash': True},
        'cuddled-lists': None,
        'fenced-code-blocks': None,
        'tables': None,
        'target-blank-links': None,
    }

    if code_friendly:
        extras['code-friendly'] = None
    else:
        extras['middle-word-em'] = {'allowed': False}

    if header_ids:
        extras['header-ids'] = None

    html = markdown2.markdown(text, extras=extras, safe_mode='escape')

    # Undo safe mode for <br> and comments.
    html = html.replace('&lt;br&gt;', '<br>')
    html = re.sub(r'&lt;!--(.*?)--&gt;', r'<!--\1-->', html, flags=re.DOTALL)

    return html

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

    # A workaround for fenced code blocks not being separated from lists in safe mode.
    text = re.sub(r'^```(.*?)```', r'<!-- CODE_MARKER -->\n\g<0>', text, flags=re.MULTILINE | re.DOTALL)

    html = markdown2.markdown(text, extras=extras, safe_mode='escape')

    # Undo safe mode for <br> and comments.
    html = html.replace('&lt;br&gt;', '<br>')
    html = re.sub(r'&lt;!--(.*?)--&gt;', r'<!--\1-->', html, flags=re.DOTALL)

    # Other replacements which aren't handled by markdown2 safe mode.
    html = html.replace('&lt;code>', '<code>')
    html = html.replace('&lt;/code>', '</code>')

    return html

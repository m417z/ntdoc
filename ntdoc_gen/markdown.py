"""Markdown processing utilities."""

import markdown2

MARKDOWN2_EXTRAS = {
    'breaks': {'on_backslash': True},
    'cuddled-lists': None,
    'fenced-code-blocks': None,
    'header-ids': None,
    'target-blank-links': None,
    'tables': None,
}


def markdown_to_html(text: str) -> str:
    return markdown2.markdown(text, extras=MARKDOWN2_EXTRAS)

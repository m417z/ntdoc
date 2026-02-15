"""Markdown processing utilities."""

import re
import secrets

import cmarkgfm

BR_SENTINEL = secrets.token_hex(8)


def markdown_to_html(text: str) -> str:
    # Preserve <br /> tags.
    text = re.sub(r'<br\s*/?>', BR_SENTINEL, text)

    html: str = cmarkgfm.markdown_to_html_with_extensions(
        text,
        extensions=[
            'autolink',
            'table',
        ],
    )

    # Make links open in new tabs.
    html = re.sub(r'<a\b', r'<a rel="noopener" target="_blank"', html)

    # Restore <br /> tags.
    html = html.replace(BR_SENTINEL, '<br />')

    return html

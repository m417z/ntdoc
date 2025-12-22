"""Markdown processing utilities."""

import re
import secrets

import cmarkgfm

BR_SENTINEL = secrets.token_hex(8)


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
    # Preserve <br /> tags.
    text = re.sub(r'<br\s*/?>', BR_SENTINEL, text)

    html: str = cmarkgfm.markdown_to_html_with_extensions(
        text,
        extensions=[
            'table',
        ],
    )

    # Make links open in new tabs.
    html = re.sub(r'<a\b', r'<a rel="noopener" target="_blank"', html)

    # Restore <br /> tags.
    html = html.replace(BR_SENTINEL, '<br />')

    # Remove code class attributes for now. TODO: remove.
    html = re.sub(r'<pre><code( class="[^"]+")?>\s*', '<pre><code>', html)

    # Temporary, TODO: remove.
    html = re.sub(r'<li>(.*?)</li>', r'<li>\n\1\n</li>', html)

    return html

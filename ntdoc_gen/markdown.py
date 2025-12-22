"""Markdown processing utilities."""

import re
import secrets

import cmarkgfm
from cmarkgfm.cmark import Options as cmarkgfmOptions

BR_SENTINEL = secrets.token_hex(8)


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
    # Preserve <br /> tags.
    text = re.sub(r'<br\s*/?>', BR_SENTINEL, text)

    html: str = cmarkgfm.markdown_to_html_with_extensions(
        text,
        options=(
            cmarkgfmOptions.CMARK_OPT_GITHUB_PRE_LANG | cmarkgfmOptions.CMARK_OPT_UNSAFE
        ),
        extensions=[
            'table',
        ],
    )

    # Make links open in new tabs.
    html = re.sub(r'<a\b', r'<a rel="noopener" target="_blank"', html)

    # Restore <br /> tags.
    html = html.replace(BR_SENTINEL, '<br />')

    return html

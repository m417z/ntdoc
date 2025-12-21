"""Markdown processing utilities."""

import re

import cmarkgfm
from cmarkgfm.cmark import Options as cmarkgfmOptions


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
    html: str = cmarkgfm.markdown_to_html_with_extensions(
        text,
        options=cmarkgfmOptions.CMARK_OPT_GITHUB_PRE_LANG,
        extensions=[
            'table',
        ],
    )

    # Make links open in new tabs.
    html = re.sub(r'<a\b', r'<a rel="noopener" target="_blank"', html)

    return html

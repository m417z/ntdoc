"""Markdown processing utilities."""

import cmarkgfm
from cmarkgfm.cmark import Options as cmarkgfmOptions


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
    return cmarkgfm.markdown_to_html_with_extensions(
        text,
        options=cmarkgfmOptions.CMARK_OPT_GITHUB_PRE_LANG,
        extensions=[
            'table',
        ],
    )
"""Markdown processing utilities."""

import re

import bleach
import cmarkgfm
from cmarkgfm.cmark import Options as cmarkgfmOptions

ALLOWED_ATTRIBUTES: dict[str, list[str]] = {
    **bleach.sanitizer.ALLOWED_ATTRIBUTES,
    'a': [
        *bleach.sanitizer.ALLOWED_ATTRIBUTES.get('a', []),
        'rel',
        'target',
    ],
    'pre': ['lang'],
    'td': ['align'],
    'th': ['align'],
    'img': ['src', 'alt', 'title'],
    'ol': ['start'],
}


def attributes_filter(tag: str, name: str, value: str) -> bool:
    allowed_attrs = ALLOWED_ATTRIBUTES.get(tag, [])
    if name in allowed_attrs:
        return True
    print(f'Warning: Disallowed attribute "{name}" on <{tag}> tag.')
    return False


cleaner = bleach.Cleaner(
    tags={
        *bleach.sanitizer.ALLOWED_TAGS,
        'p',
        'pre',
        'code',
        'span',
        'h1',
        'h2',
        'h3',
        'h4',
        'h5',
        'h6',
        'table',
        'thead',
        'tbody',
        'tr',
        'th',
        'td',
        'hr',
        'br',
        'img',
    },
    attributes=attributes_filter,
    strip_comments=False,
)


def markdown_to_html(text: str, header_ids=True, code_friendly=False) -> str:
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

    html = cleaner.clean(html)

    return html

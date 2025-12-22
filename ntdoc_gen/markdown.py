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

    # if header_ids:
    #     extras['header-ids'] = None

    html = markdown2.markdown(text, extras=extras, safe_mode='escape')

    # Undo safe mode for <br> and comments.
    html = html.replace('&lt;br&gt;', '<br>')
    html = re.sub(r'&lt;!--(.*?)--&gt;', r'<!--\1-->', html, flags=re.DOTALL)

    # Fix a specific common quirk.
    html = re.sub(r'<strong>(\w+)\*(\w+)</strong>\*', r'<strong>\1<em>\2</em></strong>', html)

    # Remove leading whitespace.
    html = re.sub(r'(?m)^[ \t]+', '', html)

    html = re.sub(r'<li>(.*?)</li>', r'<li>\n\1\n</li>', html)

    # Normalize self-closing tags.
    html = re.sub(r'<br\s*/?>', '<br />', html)
    html = re.sub(r'<hr\s*/?>', '<hr />', html)
    html = re.sub(r'<img([^>]*)>', r'<img\1 />', html)

    # Remove multiple newlines outside of <pre> blocks.
    def newlines_sub(match: re.Match) -> str:
        start_index = match.start()
        pre_open_count = html.count('<pre', 0, start_index)
        pre_end_count = html.count('</pre>', 0, start_index)
        if pre_open_count > pre_end_count:
            # Inside a pre block.
            return match.group(0)
        return f'\n'

    html = re.sub(r'\n{2,}', newlines_sub, html)

    return html

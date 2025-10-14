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

    # Encode some escaped symbols as markdown2 doesn't handle them correctly.
    def bracket_escape(m: re.Match) -> str:
        # Skip if inside of a code block.
        code_block_count = text.count('```', 0, m.start())
        if code_block_count % 2 == 1:
            return m.group(0)

        # Skip if line inside of an inline code span.
        line_start = text.rfind('\n', 0, m.start()) + 1
        backtick_count = text.count('`', line_start, m.start())
        if backtick_count % 2 == 1:
            return m.group(0)

        # Skip if escaped with an odd number of backslashes.
        preceding_text = text[:m.start()]
        trailing_backslashes = 0
        for char in reversed(preceding_text):
            if char == '\\':
                trailing_backslashes += 1
            else:
                break
        if trailing_backslashes % 2 == 1:
            return m.group(0)

        symbol = m.group(1)
        if symbol == '<':
            return '&lt;'
        elif symbol == '>':
            return '&gt;'
        else:
            assert symbol == '&'
            return '&amp;'

    text = re.sub(r'\\(?!<br>)([<>&])', bracket_escape, text)

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

import re
from pathlib import Path


def to_markdown(name: str, html: str) -> str:
    html_ = html
    html = re.sub(r'^.*?<PRE CLASS="FnDefinition">(.+?)</PRE>', '', html, flags=re.DOTALL)
    assert html != html_

    html_ = html
    html = re.sub(r'<HR WIDTH="0" SIZE="0" NOSHADE CLASS="page">(</DD></LI>)?\s*</BODY>.*$', '', html, flags=re.DOTALL)
    assert html != html_

    html = re.sub(r'<BR><BR><BR>\n<DT CLASS="Require">Supported on system versions:</DT>\n<DD><STRONG>.*?</STRONG></DD>\n', '', html)
    assert 'Supported on system versions' not in html

    parts = re.split(r'<(?:DT|DIV) CLASS="Require">', html)
    assert not any('CLASS="Require"' in part for part in parts)

    body = parts[0]

    body = re.sub(r'^(\s*<BR>)*\s*', '', body, flags=re.IGNORECASE)
    body = re.sub(r'(\s*(<BR>|</PRE>))*\s*$', '', body, flags=re.IGNORECASE)
    body = body.removeprefix('<PRE>')
    body = re.sub(r'<B><U>(\w+)</B></U>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<B><U>(\w+)</U></B>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<U><I>([^<>\n]+)</I></U>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<I><U>([^<>\n]+)</I></U>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<B><I>([^<>\n]+)</B></I>', r'**\1**', body, flags=re.IGNORECASE)
    body = re.sub(r'<B><I>([^<>\n]+)</I></B>', r'**\1**', body, flags=re.IGNORECASE)
    body = re.sub(r'<B>([^<>\n]+) </B>', r'`\1` ', body, flags=re.IGNORECASE)
    body = re.sub(r'<B>([^<>\n]+)</B>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<B>([^<>\n]+?)\s*\n</B>', r'`\1`\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<U>([^<>\n]+)</U>', r'**\1**', body, flags=re.IGNORECASE)
    body = re.sub(r'<U>([^<>\n]+?)\s*\n</U>', r'**\1**\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<EM>(\w+)</EM>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<EM>(_KiUserApcDispatcher@20)</EM>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<I>([^<>\n]+) </I>', r'*\1* ', body, flags=re.IGNORECASE)
    body = re.sub(r'<I>([^<>\n]+)</I>', r'*\1*', body, flags=re.IGNORECASE)
    body = re.sub(r'<I>([^<>\n]+?)\s*\n</I>', r'*\1*\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<FONT CLASS="ParamNameDesc">([\w.]+) </FONT>', r'`\1` ', body, flags=re.IGNORECASE)
    body = re.sub(r'<FONT CLASS="ParamNameDesc">([\w.]+)</FONT>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<A href=".*?">(\w+)</A>', r'`\1`', body, flags=re.IGNORECASE)
    body = re.sub(r'<A href=".*?">(\w+) </A>', r'`\1` ', body, flags=re.IGNORECASE)
    body = re.sub(r'<A name="\w+">(.*?)</A>', r'\1', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<A name="\w+">', r'', body, flags=re.IGNORECASE)
    body = re.sub(r'<H6></H6>', r'', body, flags=re.IGNORECASE)
    body = re.sub(r'<H6>(?:</DD>)?(?:<LI>)?([^<>\n]+)</H6>', r'\n\n### \1\n\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<DIV CLASS="reg">([^<>\n]+)</DIV>', r'\1\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<DIV CLASS="reg">([^<>\n]*)\n+</DIV>', r'\1', body, flags=re.IGNORECASE)
    body = re.sub(r'<FONT COLOR="Red">([^<>\n]+)</FONT>', r'**\1**', body, flags=re.IGNORECASE)
    body = re.sub(r'<FONT COLOR="Red">([^<>\n]+)\n</FONT>', r'**\1**\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<B><I><FONT COLOR=FF0000 SIZE=12><HR WIDTH="40%">\n</B></I></FONT>', '\n\n---\n\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<FONT COLOR=FF0000 SIZE=12><HR WIDTH="40%">\n</FONT>', '\n\n---\n\n', body, flags=re.IGNORECASE)
    body = re.sub(r'<HR WIDTH="40%">', '\n\n---\n\n', body, flags=re.IGNORECASE)
    body = re.sub(r'&nbsp;&nbsp;&nbsp;&nbsp;', '', body, flags=re.IGNORECASE)
    body = re.sub(r'(?:<UL(?: TYPE="circle")?>[ \t]*(?:<B>)?)?\n?[ \t]*<LI>', r'\n* ', body, flags=re.IGNORECASE)

    body = body.replace('\n- ???', '\n???')
    body = body.replace('\n-???', '\n???')
    body = body.replace('<DIV CLASS="reg">', '')
    body = body.replace('</DIV>', '')
    body = body.replace('<DD CLASS="reg">', '')
    body = body.replace('</DD>', '')
    body = body.replace('</UL>', '')
    body = body.replace('<B>\n</B>', '')
    body = body.replace('<BR>\n', '\n\n')
    body = body.replace('<BR>\n', '\n\n')
    body = body.replace('\n<BR>', '\n\n')
    body = body.replace('\n<BR>', '\n\n')
    body = body.replace('<BR>', '\n')
    body = re.sub(r'\n(<DD>)+', r'\n', body, flags=re.IGNORECASE)
    body = re.sub(r'(<TD.*?>)<DD>', r'\1', body, flags=re.IGNORECASE)

    body = re.sub(r'<TR>\s*<TD.*?>([^<>\n]+)</TD>\s*<TD.*?>(:[^<>\n]+)</TD>\s*</TR>', r'* \1\2', body, flags=re.IGNORECASE)
    body = body.replace('<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">\n', '\n')
    body = body.replace('\n</TABLE>', '\n')

    body = re.sub(r'^[ \t]+$', r'', body, flags=re.MULTILINE)
    body = re.sub(r'([^\n]) *\n([^\n])', r'\1 \\\n\2', body, flags=re.IGNORECASE)
    body = re.sub(r'^(\* .*) \\$', r'\1', body, flags=re.MULTILINE)
    body = re.sub(r' \\(\n\* )', r'\n\1', body)
    body = re.sub(r'^(\* .*)\n([^\n])', r'\1\n\n\2', body, flags=re.MULTILINE)

    body = re.sub(r'\n\n\n+', r'\n\n', body, flags=re.IGNORECASE)

    body = body.replace('\n\n---\n\n### ', '\n\n### ')
    body = body.replace('&lt;', '\\<')
    body = body.replace('&gt;', '\\>')
    body = re.sub(r'`\\<([^`]+)\\>`', r'`<\1>`', body, flags=re.MULTILINE)
    body = body.replace('&nbsp;', ' ')

    markdown = body.strip()

    for part in parts[1:]:
        if part.startswith('Documented by:'):
            part = part.removeprefix('Documented by:')
            part = part.removeprefix('</DT>')
            part = re.sub(r'(\s*<BR>)*\s*$', '', part).strip()
            part = re.sub(r'<DD><STRONG>(.*?)</STRONG>(:?</DD>)?', r'* \1', part, flags=re.IGNORECASE)
            part = part.replace('Reactos', 'ReactOS')
            part = part.strip()

            assert '<' not in part, part
            markdown += '\n\n# Documented by\n\n' + part
            continue

        if part.startswith('Requirements:'):
            part = re.sub(r'(\s*<BR>)*\s*$', '', part).strip()
            part_ = part
            part = re.sub(r'^Requirements:</DIV>\n<DD\s*(CLASS="req")?\s*>\s*Library:\s*<STRONG\s*(CLASS="req")?\s*>ntdll\.lib</STRONG>\s*(</DD>)?', '', part)
            assert part != part_, part

            if part != '':
                part = re.sub(r'<STRONG\s*(CLASS="req")?\s*>(\w+)</STRONG>', r'`\2`', part, flags=re.IGNORECASE)
                part = part.replace('\n', '').replace('<DD>', '\n').strip()
                part = part.replace('<DD CLASS="req" >', '')
                part = part.replace('</DD>', '')
                part = part.replace('Privileges', 'Privilege')
                part = re.sub(r'[ \t]+', r' ', part, flags=re.IGNORECASE)
                part = part.strip()

                assert '<' not in part, part
                markdown += '\n\n# Requirements\n\n' + part

            continue

        if part.startswith('See also:') or part.startswith('See Also:'):
            part = part.removeprefix('See also:</DIV>')
            part = part.removeprefix('See Also:</DIV>')
            part = part.replace('<B>', '').replace('</B>', '')
            part = re.sub(r'(?:<DD(?: CLASS="req")?>)?<A HREF=".*?">(.*?)</A>(?:<BR>)?(?:</DD>)?', r'* `\1`', part, flags=re.IGNORECASE)
            part = part.strip()

            if part != '':
                assert '<' not in part, part
                markdown += '\n\n# See also\n\n' + part

            continue

        if part.startswith('Example results:'):
            assert name == 'LdrQueryProcessModuleInformation'
            # Fix manually...
            markdown += '\n\n# Example results\n\n' + part
            continue

        assert False, part

    return markdown


def main():
    data = {}
    for file in Path('data').rglob('*.html'):
        name = file.stem
        if name in ['aindex', 'OtherObjectFunctions']:
            continue

        # print(name)

        html = file.read_text()
        if html == '404: File not found.':
            continue

        markdown = to_markdown(name, html)
        if markdown:
            data[name] = markdown

            if '<' in markdown:
                print(f'Fix manually: {name}')

    # Path('data.md').write_text('\n\n'.join(f'# {name}\n\n{markdown}' for name, markdown in data.items()))

    descriptions_path = Path('..', '..', 'descriptions')

    descriptions_with_content_before = set()
    for description_file in descriptions_path.glob('*.md'):
        description = description_file.read_text()
        if description == '':
            continue

        match = re.match(r'^This \w+ is \[?documented .*$\n?', description)
        if match:
            continue

        descriptions_with_content_before.add(description_file.stem)

    descriptions_with_content_written = set()

    for name, markdown in data.items():
        description_file = descriptions_path / f'{name.lower()}.md'
        if not description_file.exists():
            print(f'Skipping {name}')
            continue

        with open(description_file, 'r', encoding='utf-8') as f:
            first_line = f.readline().rstrip('\n')

        match = re.match(r'^This \w+ is \[?documented ', first_line)
        if not match:
            first_line = None
        else:
            if not first_line.endswith('.'):
                first_line += '.'

        new_content = ''
        if first_line:
            new_content += first_line + '\n\n---\n\n'

        new_content += markdown + '\n'

        description_file.write_text(new_content)
        descriptions_with_content_written.add(description_file.stem)

    added = descriptions_with_content_written - descriptions_with_content_before
    print(f'Added {len(added)} descriptions:')
    print('\n'.join(sorted(added)))

    untouched = descriptions_with_content_before - descriptions_with_content_written
    print(f'Untouched {len(untouched)} descriptions:')
    print('\n'.join(sorted(untouched)))


if __name__ == '__main__':
    main()

"""C/C++ header file parsing functions."""

import re
from pathlib import Path
from typing import List, Optional, Tuple

from .chunk import Chunk, ChunkOrigin


def rstrip_line_with_comment(code: str) -> str:
    if '//' in code:
        return code[:code.index('//')].rstrip()
    return code.rstrip()


def pop_next_chunk_custom_marker(code: list[str]) -> str:
    return code.pop(0)


def pop_next_chunk_macro(code: list[str]) -> str:
    macro = code.pop(0)
    while macro.rstrip('\n').endswith('\\'):
        macro += code.pop(0)
    return macro


def starts_with_struct_union(code: list[str]) -> bool:
    line = code[0]
    if match := re.fullmatch(r'_Struct_size_bytes_\(.+?\)\s*', line):
        line = code[1]

    return re.match(r'typedef\s+(DECLSPEC_ALIGN\(\d+\)\s+)?(struct|union|enum)\b', line) is not None


def pop_next_chunk_struct_union(code: list[str]) -> str:
    line = code.pop(0)
    chunk = line
    if rstrip_line_with_comment(line).endswith(';'):
        return chunk

    assert ';' not in rstrip_line_with_comment(line), line

    while True:
        line = code.pop(0)
        chunk += line
        if line.startswith('}'):
            break

    last_char = line.rstrip('\n')[-1]
    while last_char != ';':
        assert last_char == ',', line
        line = code.pop(0)
        chunk += line
        last_char = line.rstrip('\n')[-1]

    return chunk


def starts_with_function_definition(code: list[str]) -> bool:
    had_brackets = False
    for line in code:
        line = rstrip_line_with_comment(line)

        if '(' in line:
            had_brackets = True

        if ')' in line:
            assert had_brackets

        if line.endswith(';'):
            return False
        assert ';' not in line, line

        if '{' in line:
            assert line.endswith('{'), line
            return had_brackets

    assert False, code


def get_function_identifier(chunk: str) -> str:
    if match := re.search(r'\{\s*(?://.*)?$', chunk, flags=re.MULTILINE):
        chunk = chunk[:match.start()]
    elif match := re.search(r';\s*(?://.*)?$', chunk, flags=re.MULTILINE):
        chunk = chunk[:match.start()]
    else:
        assert False, chunk

    assert ';' not in chunk, chunk
    assert '{' not in chunk, chunk

    if match := re.findall(r'(\w+)\s*\(', chunk):
        match = [m for m in match if m not in [
            '_Always_',
            '_At_',
            '_Deref_out_range_',
            '_In_range_',
            '_In_reads_',
            '_In_reads_bytes_',
            '_In_reads_opt_',
            '_In_reads_or_z_',
            '_Inout_updates_',
            '_Inout_updates_bytes_',
            '_Old_',
            '_Out_writes_',
            '_Out_writes_bytes_',
            '_Out_writes_bytes_all_',
            '_Out_writes_bytes_opt_',
            '_Out_writes_to_',
            '_Outptr_opt_result_buffer_',
            '_Outptr_opt_result_bytebuffer_',
            '_Outptr_result_buffer_',
            '_Post_equal_to_',
            '_Post_satisfies_',
            '_String_length_',
            '_Success_',
            '_Unchanged_',
            '_When_',
            'sizeof',
        ]]
        if len(match) == 1:
            return match[0]
        assert False, (chunk, match)

    assert False, chunk


def pop_next_chunk_function_definition(code: list[str]) -> str:
    chunk = ''
    while True:
        line = code.pop(0)
        chunk += line
        if line.startswith('}'):
            assert line.rstrip() == '}', line
            break
    return chunk


def pop_next_chunk_default(code: list[str]) -> str:
    chunk = ''
    while True:
        line = code.pop(0)
        chunk += line
        if rstrip_line_with_comment(line).endswith(';'):
            break
        assert ';' not in rstrip_line_with_comment(line), line
    return chunk


def pop_next_chunk(code: list[str]) -> Optional[Tuple[str, str, int]]:
    intro = ''

    while len(code) > 0 and rstrip_line_with_comment(code[0]) == '':
        line = code.pop(0)
        if intro == '' and line.strip() == '':
            continue

        intro += line

    lines_left = len(code)
    if lines_left == 0:
        return None

    assert not code[0].startswith(' '), code[0]

    if code[0].startswith('@'):
        chunk = pop_next_chunk_custom_marker(code)
    elif code[0].startswith('#'):
        chunk = pop_next_chunk_macro(code)
    elif starts_with_struct_union(code):
        chunk = pop_next_chunk_struct_union(code)
    elif starts_with_function_definition(code):
        chunk = pop_next_chunk_function_definition(code)
    else:
        chunk = pop_next_chunk_default(code)

    return intro, chunk, lines_left


def get_chunk_identifiers(chunk: str) -> List[str]:
    if chunk.startswith('#include'):
        # push/pop pack includes are handled separately.
        assert 'pshpack' not in chunk.lower(), chunk
        assert 'poppack' not in chunk.lower(), chunk
        return []

    if (chunk.startswith('#error') or
        chunk.startswith('#undef') or
        chunk.startswith('#define PHNT_') or
        chunk.startswith('C_ASSERT(') or
        chunk.startswith('static_assert(') or
        chunk.startswith('static_assert (') or
        chunk.startswith('#pragma region') or
        chunk.startswith('#pragma endregion') or
        chunk.startswith('#pragma warning') or
        chunk.startswith('#pragma prefast') or
        chunk.startswith('#pragma intrinsic') or
        chunk.startswith('#pragma deprecated') or
        chunk.startswith('#pragma comment(lib,') or
        chunk.rstrip() == '#pragma once'):
        return []

    # Remove comments and noise, then strip.
    chunk = re.sub(r'\s*//.*$', '', chunk, flags=re.MULTILINE)
    # For WNF_USER_CALLBACK:
    chunk = chunk.replace('_Always_(_Post_satisfies_(return == STATUS_NO_MEMORY || return == STATUS_RETRY || return == STATUS_SUCCESS))', '')
    chunk = chunk.strip()

    if re.fullmatch(r'#define +\w+', chunk):
        return []

    if match := re.match(r'#define +(\w+)[( ]', chunk):
        return [match.group(1)]

    assert not chunk.startswith('#define '), chunk

    if re.match(r'(?:_Struct_size_bytes_\(.+?\)\s+)?typedef\s+(?:DECLSPEC_ALIGN\(\d+\)\s+)?(struct|union|enum)\b', chunk):
        last_index = chunk.rfind('}')
        if last_index != -1:
            assert '{' in chunk, chunk
            idents = chunk[last_index + 1:]
            assert idents.endswith(';'), chunk
            idents = idents.removesuffix(';')

            ident_full = None
            match = re.search(r'^typedef (?:DECLSPEC_ALIGN\(\d+\) )?(struct|union|enum) .*?(\w+)\s*\{', chunk, flags=re.MULTILINE)
            assert match, chunk
            assert not match.group(2).startswith('DECLSPEC'), chunk
            ident_full = match.group(1) + ' ' + match.group(2)
        else:
            # Forward declaration.
            assert '{' not in chunk, chunk
            match = re.fullmatch(r'typedef (struct|union|enum) (\w+)(.*);', chunk)
            assert match, chunk
            ident_full = match.group(1) + ' ' + match.group(2)
            idents = match.group(3)

        idents = idents.split(',')
        idents = [re.sub(r'^(\s*(FAR\s*)?\*)+', '', x).strip() for x in idents]
        assert len(idents) > 0, chunk
        assert all(re.fullmatch(r'\w+', x) for x in idents), idents
        return idents + ([ident_full] if ident_full is not None else [])

    # Special cases.
    if chunk == 'typedef _Return_type_success_(return >= 0) LONG NTSTATUS;':
        return ['NTSTATUS']
    if chunk == 'typedef _Return_type_success_(return >= 0) long NTSTATUS;':
        return ['NTSTATUS']
    if chunk == 'typedef NTSTATUS FN_DISPATCH(PVOID);':
        return ['FN_DISPATCH']

    if match := re.match(r'(typedef\s+)_Function_class_\((\w+)\)', chunk):
        ident = match.group(2)
        chunk = re.sub(r'(typedef\s+)_Function_class_\((\w+)\)', r'\g<1>', chunk)

        # Example:
        # typedef _Function_class_(PROCESSOR_IDLE_HANDLER)
        # NTSTATUS FASTCALL PROCESSOR_IDLE_HANDLER(...
        if match := re.match(r'typedef\s+(?:\w+\s+NTAPI\s+|NTSTATUS\s+(?:(?:FASTCALL|STDAPIVCALLTYPE)\s+)?)(\w+)\(', chunk):
            assert match.group(1) == ident, (match.group(1), ident)
        else:
            assert False, chunk

        return [ident]

    assert '_Function_class_' not in chunk, chunk

    if chunk.startswith('typedef'):
        # Example:
        # typedef VOID (NTAPI *PACTIVATION_CONTEXT_NOTIFY_ROUTINE)(...
        if match := re.search(r'\((?:NTAPI|__cdecl|FASTCALL|WINAPI|STDAPIVCALLTYPE)\s*(?:\*\s*)?(\w+)\)', chunk):
            return [match.group(1)]

    # Example:
    # typedef PVOID SAM_HANDLE, *PSAM_HANDLE;
    if match := re.fullmatch(r'typedef(?:\s+(?:const|CONST|signed|unsigned|\[public\]|_W64|_Null_terminated_))*\s+\w+(?: const| CONST| UNALIGNED)*\s*(.*?)(?:\[.*?\])?;', chunk):
        idents = match.group(1).split(',')
        idents = [x.lstrip('* ').rstrip() for x in idents]
        assert len(idents) > 0, chunk
        assert all(re.fullmatch(r'\w+', x) for x in idents), idents
        return idents

    assert 'typedef' not in chunk, chunk

    if match := re.search(r'(?:NTAPI|NTAPI_INLINE)\s+(\w+)\s*\(', chunk):
        return [match.group(1)]

    assert 'NTAPI' not in chunk, chunk

    if chunk == 'EXTERN_C IMAGE_DOS_HEADER __ImageBase;':
        return ['__ImageBase']

    if match := re.match(r'DEFINE_GUID\(\s*(\w+),', chunk):
        return [match.group(1)]

    if match := re.match(r'EXTERN_C DECLSPEC_SELECTANY CONST GUID (\w+) =', chunk):
        return [match.group(1)]

    if match := re.fullmatch(r'NTSYSAPI \w+ (\w+);', chunk):
        return [match.group(1)]

    if match := re.fullmatch(r'(?:enum|struct) (\w+);', chunk):
        return [match.group(1)]

    if match := re.match(r'(DEFINE_ENUM_FLAG_OPERATORS|C_ASSERT)\s*\(', chunk):
        return []

    if match := re.match(r'\s*(\w+)\s*\(', chunk):
        assert match.group(1) in [
            '_At_',
            '_Post_satisfies_',
            '_Success_',
            '_When_',
        ], chunk

    # Functions.
    if ident := get_function_identifier(chunk):
        return [ident]

    assert False, chunk


def split_header_to_chunks(path: Path) -> List[Chunk]:
    code = path.read_text()
    original_newline_count = code.count('\n')

    # Tabs to spaces, only at the beginning of the line.
    code = re.sub(r'^\t+', lambda x: 4 * ' ' * len(x.group(0)), code, flags=re.MULTILINE)

    # Make sure no tabs are left.
    assert '\t' not in code

    # Make sure no line starts with @, which is used as a marker.
    assert not re.search(r'^\s*@', code, flags=re.MULTILINE)

    # Remove block comments at the top of the file.
    code = re.sub(r'^/\*.*?\*/', lambda x: re.sub(r'[^\n]', '', x.group(0)), code, flags=re.DOTALL)

    # Turn block comments into single-line comments with markers for easier parsing.
    assert '//@' not in code  # Used as a marker.
    code = re.sub(
        r'/\*.*?\*/ *$',
        lambda x: '\n'.join([f'//@{line}' for line in x.group(0).split('\n')]),
        code,
        flags=re.DOTALL | re.MULTILINE,
    )
    assert '/*' not in re.sub(r'//.*', '', code)
    assert '*/' not in re.sub(r'//.*', '', code)

    # Remove extern "C" declarations.
    code = code.replace('\n#ifdef __cplusplus\nextern "C" {\n#endif\n', '\n\n\n\n')
    code = code.replace('\n#ifdef __cplusplus\n}\n#endif\n', '\n\n\n\n')
    code = code.replace('\nEXTERN_C_START\n', '\n\n')
    code = code.replace('\nEXTERN_C_END\n', '\n\n')

    # Remove leading spaces for PHNT_MODE defines.
    code = re.sub(r'^[ \t]+(#define PHNT_MODE )', r'\1', code, flags=re.MULTILINE)

    # Remove other stuff.
    code = code.replace('\n// Options\n\n//#define PHNT_NO_INLINE_INIT_STRING\n', '\n\n\n\n')

    code = code.replace(R"""#ifdef __cplusplus
extern "C++"
{
template <size_t N> char _RTL_CONSTANT_STRING_type_check(const char  (&s)[N]);
template <size_t N> char _RTL_CONSTANT_STRING_type_check(const WCHAR (&s)[N]);
// __typeof would be desirable here instead of sizeof.
template <size_t N> class _RTL_CONSTANT_STRING_remove_const_template_class;
template <> class _RTL_CONSTANT_STRING_remove_const_template_class<sizeof(char)>  {public: typedef  char T; };
template <> class _RTL_CONSTANT_STRING_remove_const_template_class<sizeof(WCHAR)> {public: typedef WCHAR T; };
#define _RTL_CONSTANT_STRING_remove_const_macro(s) \
    (const_cast<_RTL_CONSTANT_STRING_remove_const_template_class<sizeof((s)[0])>::T*>(s))
}
#else
char _RTL_CONSTANT_STRING_type_check(const void *s);
#define _RTL_CONSTANT_STRING_remove_const_macro(s) (s)
#endif
""", "\n" * 16)

    # Add custom markers.
    code = re.sub(r'^// (begin|end)_', r'@\g<0>', code, flags=re.MULTILINE)
    code = re.sub(r'^#include <(pshpack\d+|poppack)\.h>$', r'@\g<0>', code, flags=re.MULTILINE)

    # Make sure we didn't mess up the line count for line number tracking.
    assert code.count('\n') == original_newline_count

    code = code.splitlines(keepends=True)
    code_lines_total = len(code)

    chunks: List[Tuple[str, str, int]] = []
    while True:
        next_chunk = pop_next_chunk(code)
        if next_chunk is None:
            break

        intro, body, lines_left = next_chunk
        line_number = code_lines_total - lines_left + 1

        chunks.append((intro, body, line_number))

    result: List[Chunk] = []

    before: List[Tuple[str, str]] = []
    after: List[str] = []
    for intro, body, line_number in chunks:
        if body.startswith('#if'):
            before.append((intro, body))
            after.insert(0, '#endif\n')
            continue

        if body.startswith('@// begin_'):
            before.append((intro, body[1:]))
            after.insert(0, re.sub(r'^@// begin_(\w+).*$', r'// end_\1', body))
            continue

        if body.startswith('@#include <pshpack'):
            before.append((intro, body[1:]))
            after.insert(0, '#include <poppack.h>\n')
            continue

        if body.startswith('#endif'):
            _, popped_before = before.pop()
            popped_after = after.pop(0)
            assert popped_before.startswith('#if'), popped_before
            assert popped_after.startswith('#endif'), popped_after
            continue

        if body.startswith('@// end_'):
            _, popped_before = before.pop()
            popped_after = after.pop(0)
            assert popped_before.startswith('// begin_'), popped_before
            assert popped_after.startswith('// end_'), popped_after
            continue

        if body.startswith('@#include <poppack.h>'):
            _, popped_before = before.pop()
            popped_after = after.pop(0)
            assert popped_before.startswith('#include <pshpack'), popped_before
            assert popped_after.startswith('#include <poppack.h>'), popped_after
            continue

        if body.startswith('#else'):
            popped_before_intro, popped_before = before.pop()
            assert popped_before.startswith('#if'), popped_before
            before.append((popped_before_intro, popped_before + '// ...\n' + body))
            continue

        if body.startswith('#elif '):
            popped_before_intro, popped_before = before.pop()
            assert popped_before.startswith('#if '), popped_before
            before.append((intro, popped_before + '// ...\n' + body))
            continue

        idents = get_chunk_identifiers(body)
        if len(idents) == 0:
            continue

        def remove_markers(code: str):
            return re.sub(r'//@', '', code)

        code_url = f'{path.name}#L{line_number}'

        result.append(Chunk(
            origin=ChunkOrigin.PHNT,
            code_url=code_url,
            idents=idents,
            before=[(remove_markers(x), remove_markers(y)) for x, y in before],
            intro=remove_markers(intro),
            body=remove_markers(body),
            after=[remove_markers(x) for x in after],
        ))

    assert len(before) == 0, before
    assert len(after) == 0, after

    return result

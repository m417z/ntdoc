import argparse
import json
import re
import shutil
import time
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import markdown2

URL_PHNT_REPOSITORY = 'https://github.com/winsiderss/systeminformer'
URL_DESCRIPTIONS = 'https://github.com/m417z/ntdoc/blob/main/descriptions'
PHNT_REPOSITORY_COMMIT = 'master'  # Updated from command line.

MARKDOWN2_EXTRAS = {
    'breaks': {'on_backslash': True},
    'cuddled-lists': None,
    'fenced-code-blocks': None,
    'header-ids': None,
    'target-blank-links': None,
    'tables': None,
}


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
    if line.rstrip('\n') == '_Struct_size_bytes_(sizeof(SYSTEM_POWER_STATE_DISABLE_REASON) + PowerReasonLength)':
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
            assert line == '{', line
            return had_brackets

    assert False, code


def get_function_identifier(chunk: str) -> str:
    if match := re.search(r'^{\s*(?://.*)?$', chunk, flags=re.MULTILINE):
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

    if re.match(r'(?:_Struct_size_bytes_\(.*?\)\s+)?typedef\s+(?:DECLSPEC_ALIGN\(\d+\)\s+)?(struct|union|enum)\b', chunk):
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

    if match := re.match(r'(typedef\s+)_Function_class_\((\w+)\)', chunk):
        ident = match.group(2)
        chunk = re.sub(r'(typedef\s+)_Function_class_\((\w+)\)', r'\g<1>', chunk)

        # Example:
        # typedef _Function_class_(PROCESSOR_IDLE_HANDLER)
        # NTSTATUS FASTCALL PROCESSOR_IDLE_HANDLER(...
        if match := re.match(r'typedef\s+(?:\w+\s+NTAPI\s+|NTSTATUS\s+(?:FASTCALL\s+)?)(\w+)\(', chunk):
            assert match.group(1) == ident, (match.group(1), ident)
        else:
            assert False, chunk

        return [ident]

    assert '_Function_class_' not in chunk, chunk

    if chunk.startswith('typedef'):
        # Example:
        # typedef VOID (NTAPI *PACTIVATION_CONTEXT_NOTIFY_ROUTINE)(...
        if match := re.search(r'\((?:NTAPI|__cdecl|FASTCALL|WINAPI)\s*(?:\*\s*)?(\w+)\)', chunk):
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

    if chunk == 'EXTERN_C CONST IMAGE_DOS_HEADER __ImageBase;':
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


@dataclass
class Chunk:
    header_name: str
    line_number: int
    idents: List[str]
    before: List[Tuple[str, str]]
    intro: str
    body: str
    after: List[str]


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

    chunks = []
    while True:
        next_chunk = pop_next_chunk(code)
        if next_chunk is None:
            break

        intro, body, lines_left = next_chunk
        line_number = code_lines_total - lines_left + 1

        chunks.append((intro, body, line_number))

    result: List[Chunk] = []

    before = []
    after = []
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

        result.append(Chunk(
            path.name,
            line_number,
            idents,
            [(remove_markers(x), remove_markers(y)) for x, y in before],
            remove_markers(intro),
            remove_markers(body),
            [remove_markers(x) for x in after],
        ))

    assert len(before) == 0, before
    assert len(after) == 0, after

    return result


def remove_redundant_forward_declaration_chunks(chunks: List[Chunk]) -> List[Chunk]:
    def is_forward_declaration(chunk: Chunk) -> bool:
        body = chunk.body.rstrip('\n')
        return re.fullmatch(r'(typedef )?(struct|union|enum) (\w+).*;(\s*//.*)?', body) is not None

    result: List[Chunk] = []

    for chunk in chunks:
        if is_forward_declaration(chunk):
            idents_unique = set(chunk.idents)

            for chunk_other in chunks:
                if chunk_other is chunk or is_forward_declaration(chunk_other):
                    continue

                for ident in list(idents_unique):
                    if ident in chunk_other.idents:
                        idents_unique.remove(ident)

            if idents_unique == set():
                continue

        result.append(chunk)

    return result


def organize_idents_to_ids(chunks: List[Chunk]):
    ident_to_id: Dict[str, str] = {}
    id_special_cases: Dict[str, str] = {
        'FSINFOCLASS': 'FS_INFORMATION_CLASS',
        'PERFINFO_TRACE_ENTRY': 'PERFINFO_TRACE_HEADER',
        'WMI_DISKIO_READWRITE': 'ETW_DISKIO_READWRITE_V3',
        'WMI_DISKIO_FLUSH_BUFFERS': 'ETW_DISKIO_FLUSH_BUFFERS_V3',
        'MOFRESOURCEINFOA': 'MOFRESOURCEINFO',
        'MOFRESOURCEINFOW': 'MOFRESOURCEINFO',
    }
    id_update_from_to_collisions: Dict[str, str] = {
        # Collides with function WinStationShadow.
        'WINSTATIONSHADOW': 'winstationshadow-struct',
        # Collides with function ConsoleControl.
        'CONSOLECONTROL': 'consolecontrol-struct',
        # Collides with size_t (lowercase).
        'SIZE_T': 'size_t-win',
        # Collides with RtlXxxToSizeT.
        'RtlDWord64ToSIZET': 'rtldword64tosizet-win',
        'RtlDWordLongToSIZET': 'rtldwordlongtosizet-win',
        'RtlInt16ToSIZET': 'rtlint16tosizet-win',
        'RtlInt32ToSIZET': 'rtlint32tosizet-win',
        'RtlInt64ToSIZET': 'rtlint64tosizet-win',
        'RtlInt8ToSIZET': 'rtlint8tosizet-win',
        'RtlIntPtrToSIZET': 'rtlintptrtosizet-win',
        'RtlIntToSIZET': 'rtlinttosizet-win',
        'RtlLong64ToSIZET': 'rtllong64tosizet-win',
        'RtlLongLongToSIZET': 'rtllonglongtosizet-win',
        'RtlLongPtrToSIZET': 'rtllongptrtosizet-win',
        'RtlLongToSIZET': 'rtllongtosizet-win',
        'RtlPtrdiffTToSIZET': 'rtlptrdiffttosizet-win',
        'RtlShortToSIZET': 'rtlshorttosizet-win',
        'RtlSSIZETToSIZET': 'rtlssizettosizet-win',
        'RtlUInt64ToSIZET': 'rtluint64tosizet-win',
        'RtlULong64ToSIZET': 'rtlulong64tosizet-win',
        'RtlULongLongToSIZET': 'rtlulonglongtosizet-win',
        # Collides with RtlSizeTXXX.
        'RtlSIZETAdd': 'rtlsizetadd-win',
        'RtlSIZETMult': 'rtlsizetmult-win',
        'RtlSIZETSub': 'rtlsizetsub-win',
        # Collides with RtlSizeTToXXX.
        'RtlSIZETToByte': 'rtlsizettobyte-win',
        'RtlSIZETToChar': 'rtlsizettochar-win',
        'RtlSIZETToDWord': 'rtlsizettodword-win',
        'RtlSIZETToInt': 'rtlsizettoint-win',
        'RtlSIZETToInt16': 'rtlsizettoint16-win',
        'RtlSIZETToInt32': 'rtlsizettoint32-win',
        'RtlSIZETToInt64': 'rtlsizettoint64-win',
        'RtlSIZETToInt8': 'rtlsizettoint8-win',
        'RtlSIZETToIntPtr': 'rtlsizettointptr-win',
        'RtlSIZETToLong': 'rtlsizettolong-win',
        'RtlSIZETToLong64': 'rtlsizettolong64-win',
        'RtlSIZETToLongLong': 'rtlsizettolonglong-win',
        'RtlSIZETToLongPtr': 'rtlsizettolongptr-win',
        'RtlSIZETToPtrdiffT': 'rtlsizettoptrdifft-win',
        'RtlSIZETToShort': 'rtlsizettoshort-win',
        'RtlSIZETToSSIZET': 'rtlsizettossizet-win',
        'RtlSIZETToUChar': 'rtlsizettouchar-win',
        'RtlSIZETToUInt': 'rtlsizettouint-win',
        'RtlSIZETToUInt16': 'rtlsizettouint16-win',
        'RtlSIZETToUInt32': 'rtlsizettouint32-win',
        'RtlSIZETToUInt8': 'rtlsizettouint8-win',
        'RtlSIZETToULong': 'rtlsizettoulong-win',
        'RtlSIZETToUShort': 'rtlsizettoushort-win',
        'RtlSIZETToWord': 'rtlsizettoword-win',
        'SMBIOS_PROCESSOR_FAMILY_ULTRASPARC_Iii': 'smbios_processor_family_ultrasparc_iii-1',
        'SMBIOS_PROCESSOR_FAMILY_ULTRASPARC_III': 'smbios_processor_family_ultrasparc_iii-2',
    }
    id_update_from_to = id_update_from_to_collisions.copy()

    for chunk in chunks:
        id = chunk.idents[0]
        for ident in chunk.idents:
            if ident not in ident_to_id:
                ident_to_id[ident] = id
                continue

            id1 = ident_to_id[ident]
            id2 = id

            if id1 in id_special_cases and id2 == id_special_cases[id1]:
                id_update_from_to[id1] = id_special_cases[id1]
            elif id2 in id_special_cases and id1 == id_special_cases[id2]:
                id_update_from_to[id2] = id_special_cases[id2]
            else:
                assert id1 == id2, (ident, id1, id2)

    # ZwAbc and NtAbc are the same, assign the same id.
    for k in ident_to_id:
        if k.startswith('Zw'):
            nt_k = 'Nt' + k[2:]
            assert nt_k in ident_to_id, (k, nt_k)
            ident_to_id[k] = ident_to_id[nt_k]

    for k in ident_to_id:
        if ident_to_id[k] in id_update_from_to:
            ident_to_id[k] = id_update_from_to[ident_to_id[k]]

    id_lower_case_mapping = {}
    for k in ident_to_id:
        id_lower_case = ident_to_id[k].lower()
        id_original_case = ident_to_id[k]

        if id_lower_case in id_lower_case_mapping:
            assert id_lower_case_mapping[id_lower_case] == id_original_case, (
                f'Different case for {id_original_case}: {id_lower_case_mapping[id_lower_case]} vs {id_original_case}')
        else:
            id_lower_case_mapping[id_lower_case] = id_original_case

        ident_to_id[k] = id_lower_case
        assert re.fullmatch(r'[a-z0-9_]+', ident_to_id[k]) or ident_to_id[k] in id_update_from_to_collisions.values(), ident_to_id[k]

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        for ident in chunk.idents[1:]:
            assert ident_to_id[ident] == id, (ident, ident_to_id[ident], id)

    return ident_to_id


def chunk_to_html(chunk: Chunk) -> str:
    header_name = chunk.header_name
    line_number = chunk.line_number
    before = chunk.before
    intro = chunk.intro
    body = chunk.body
    after = chunk.after

    html_before = ''
    for x, y in before:
        html_before += escape(f'{x}{y}')

    # Remove empty lines.
    html_before = re.sub(r'\n\n+', '\n', html_before)

    html_before += '\n'

    html_after = ''
    for x in after:
        html_after += escape(x)

    # Remove empty lines.
    html_after = re.sub(r'\n\n+', '\n', html_after)

    html_after = '\n' + html_after

    code_url = URL_PHNT_REPOSITORY + f'/blob/{PHNT_REPOSITORY_COMMIT}/phnt/include/{header_name}#L{line_number}'

    html = '<pre class="ntdoc-code-pre">'
    html += '<code class="ntdoc-code">'
    html += '<span class="ntdoc-code-header">'
    html += html_before
    html += '</span>'
    html += '<span class="ntdoc-code-intro">'
    html += escape(intro)
    html += '</span>'
    html += '<span class="ntdoc-code-body">'
    html += escape(body)
    html += '</span>'
    html += '<span class="ntdoc-code-footer">'
    html += html_after
    html += '</span>'
    html += '<span class="ntdoc-code-links">'
    html += '<hr>'
    html += f'<a target="_blank" href="{code_url}">View code on GitHub</a>'
    html += '</span>'
    html += '</code>'
    html += '</pre>'

    return html


def html_add_id_links(html: str, ident_to_id: Dict[str, str], exclude_id: Optional[str], id_to_body: Dict[str, str]) -> str:
    # Sort by length to avoid matching substrings, e.g. "struct ABC" should
    # match before "ABC".
    ids_sorted_by_length = sorted(ident_to_id.keys(), key=lambda x: len(x), reverse=True)

    regex = rf'\b({"|".join(ids_sorted_by_length)})\b'

    def repl(match):
        ident = match.group(1)
        id = ident_to_id[ident]
        if id == exclude_id:
            return ident

        tooltip_text = id_to_body[id].strip()

        tooltip_text_lines_max = 20
        tooltip_text_lines = tooltip_text.splitlines()
        if len(tooltip_text_lines) > tooltip_text_lines_max:
            tooltip_text = '\n'.join(tooltip_text_lines[:tooltip_text_lines_max]) + '\n...'
        elif len(tooltip_text_lines) == 1:
            # Remove extra whitespace in lines such as:
            # #define FILE_CREATED                    0x00000002
            # typedef long                LONG;
            if tooltip_text.startswith('#define ') or tooltip_text.startswith('typedef '):
                tooltip_text = re.sub(r'\s+', ' ', tooltip_text)

        tooltip_text_escaped = escape(tooltip_text).replace('\n', '&#10;')

        return f'<a href="{id}" title="{tooltip_text_escaped}">{ident}</a>'

    return re.sub(regex, repl, html)


def changelog_to_html(ident_to_id: Dict[str, str], id_to_body: Dict[str, str]) -> Tuple[str, str]:
    changelog_path = Path('CHANGELOG.md')
    changelog = changelog_path.read_text()

    changelog_markdown = changelog.split('<!-- content -->', 1)[1].lstrip()
    changelog_markdown_short = changelog_markdown.split('<!-- more -->', 1)[0]

    changelog_short = '<div class="ntdoc-changelog-short">\n'
    changelog_short += '<h1>Recent content changes</h1>\n'
    changelog_short += markdown2.markdown(changelog_markdown_short, extras=MARKDOWN2_EXTRAS)
    changelog_short += '<a href="changelog">All content changes</a>\n'
    changelog_short += '</div>\n'

    # h2 -> h3, h1 -> h2.
    changelog_short = re.sub(r'(</?h)2\b', r'\g<1>3', changelog_short)
    changelog_short = re.sub(r'(</?h)1\b', r'\g<1>2', changelog_short)

    changelog_full = '<div class="ntdoc-description ntdoc-changelog-full">\n'
    changelog_full += markdown2.markdown(changelog_markdown, extras=MARKDOWN2_EXTRAS)
    changelog_full += '</div>\n'

    changelog_full = html_add_id_links(changelog_full, ident_to_id, None, id_to_body)

    return changelog_short, changelog_full


def organize_chunks_to_dir(chunks: List[Chunk], ident_to_id: Dict[str, str], assets_path: Path, out_path: Path, ids_pattern: Optional[str]):
    shutil.copytree(assets_path, out_path)

    html_page_template_path = out_path / 'page-template.html'
    html_page_template = html_page_template_path.read_text()
    html_page_template_path.unlink()

    id_to_html_contents: Dict[str, List[str]] = {}
    id_to_id_human: Dict[str, str] = {}
    id_to_body: Dict[str, str] = {}

    for chunk in chunks:
        id = ident_to_id[chunk.idents[0]]
        html = chunk_to_html(chunk)
        id_to_html_contents.setdefault(id, []).append(html)

        id_parts = id.split('-')
        assert 1 <= len(id_parts) <= 2, id
        id_to_match = id_parts[0]

        id_human_candidates = [x for x in chunk.idents if x.lower() == id_to_match.lower()]
        assert len(id_human_candidates) <= 1, (id, chunk.idents)

        if len(id_human_candidates) > 0:
            assert id not in id_to_id_human or id_to_id_human[id] == id_human_candidates[0]
            id_to_id_human[id] = id_human_candidates[0]

        if id not in id_to_body:
            id_to_body[id] = chunk.body

    for id, html_contents in id_to_html_contents.items():
        if len(html_contents) > 4:
            print(f'Warning: Many elements for {id}: {len(html_contents)}')

        if ids_pattern and not re.search(ids_pattern, id, flags=re.IGNORECASE):
            continue

        html = '<div class="ntdoc-code-elements">\n'

        for html_content in html_contents:
            html += '<div class="ntdoc-code-element">\n'
            html += html_add_id_links(html_content, ident_to_id, id, id_to_body)
            html += '</div>\n'

        html += '</div>\n'

        html += '<div class="ntdoc-description">\n'

        description_path = Path('descriptions', f'{id}.md')
        description = description_path.read_text().strip() if description_path.exists() else ''
        if description != '':
            html_description = markdown2.markdown(description, extras=MARKDOWN2_EXTRAS)

            html += html_add_id_links(html_description, ident_to_id, id, id_to_body)
        else:
            html += '<div class="ntdoc-description-none">\n'
            html += '<p>No description available.</p>\n'
            html += '</div>\n'

        html += '</div>\n'
        html += '<div class="ntdoc-description-links">\n'
        html += f'<a target="_blank" href="{URL_DESCRIPTIONS}/{id}.md">Edit description on GitHub</a>\n'
        html += '</div>\n'

        html_page = html_page_template.replace('{{id}}', id_to_id_human[id]).replace('{{content}}', html)
        (out_path / f'{id}.html').write_text(html_page)

    with (out_path / 'ident-to-id.json').open('w') as f:
        json.dump(ident_to_id, f, indent=0, sort_keys=True)

    html = ''
    for ident in sorted(ident_to_id):
        html += f'<div><a href="{ident_to_id[ident]}">{ident}</a></div>\n'

    html_page = html_page_template.replace('{{id}}', 'Symbols').replace('{{content}}', html)
    (out_path / f'symbols.html').write_text(html_page)

    changelog_short, changelog_full = changelog_to_html(ident_to_id, id_to_body)

    index_html_path = out_path / 'index.html'
    index_html_path.write_text(index_html_path.read_text().replace('{{changelog}}', changelog_short))

    html_page = html_page_template.replace('{{id}}', 'Content changes').replace('{{content}}', changelog_full)
    (out_path / f'changelog.html').write_text(html_page)


def generate_docs(phnt_include_path: Path, ids_pattern: Optional[str]):
    chunks: List[Chunk] = []
    for p in sorted(phnt_include_path.glob('*.h')):
        chunks += split_header_to_chunks(p)

    chunks = remove_redundant_forward_declaration_chunks(chunks)

    ident_to_id = organize_idents_to_ids(chunks)

    assets_path = Path('assets')
    out_path = Path('docs')
    organize_chunks_to_dir(chunks, ident_to_id, assets_path, out_path, ids_pattern)


def validate_description_files():
    descriptions_ids = set(p.stem for p in Path('descriptions').glob('*.md'))

    with Path('docs', 'ident-to-id.json').open() as f:
        docs_ids = set(json.load(f).values())

    if descriptions_ids != docs_ids:
        print('Warning: Description files and docs do not match.')
        print('To update, run:')
        print()

        non_empty = set()
        empty = set()

        for p in descriptions_ids - docs_ids:
            size = Path('descriptions', p + '.md').stat().st_size
            if size > 0:
                non_empty.add(p)
            else:
                empty.add(p)

        if non_empty:
            print('# Non-empty description files (!!!):')
            for p in sorted(non_empty):
                print(f'rm descriptions/{p}.md')

        if empty:
            print('# Empty description files:')
            for p in sorted(empty):
                print(f'rm descriptions/{p}.md')

        if docs_ids - descriptions_ids:
            print('# Missing description files:')
            for p in sorted(docs_ids - descriptions_ids):
                print(f'touch descriptions/{p}.md')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="phnt include path", required=True)
    parser.add_argument("-c", "--commit", help="phnt commit")
    parser.add_argument("-i", "--ids-pattern",
                        help="generate only the ids matching the regex pattern, "
                             "useful for testing to quickly generate a subset of the docs")
    args = parser.parse_args()

    phnt_include_path = Path(args.path)

    global PHNT_REPOSITORY_COMMIT
    if args.commit is not None:
        PHNT_REPOSITORY_COMMIT = args.commit

    start = time.time()

    generate_docs(phnt_include_path, args.ids_pattern)
    validate_description_files()

    end = time.time()
    print(f'Finished in {end - start:.2f}s')


if __name__ == '__main__':
    main()

"""C/C++ header file parsing functions."""

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import List, Optional, Tuple

from .chunk import Chunk, ChunkOrigin


class ParseError(Exception):
    pass


class TokenKind(Enum):
    # Except for DIRECTIVE, the values are the group names in TOKEN_REGEX.
    IDENT = 'ident'
    NUMBER = 'number'
    STRING = 'string'
    CHAR = 'char'
    PUNCT = 'punct'
    OTHER = 'other'
    COMMENT = 'comment'
    DIRECTIVE = 'directive'


@dataclass
class Token:
    kind: TokenKind
    text: str
    line: int  # 0-based line of the first character.
    end_line: int  # 0-based line of the last character.
    col: int
    # For a directive, its tokens after the '#', without comments.
    sub: List['Token'] = field(default_factory=lambda: list[Token]())


TOKEN_REGEX = re.compile(r'''
    (?P<ws>[^\S\n]+|\\\n)
  | (?P<nl>\n)
  | (?P<comment>//(?:[^\n\\]|\\.)*|/\*.*?\*/)
  | (?P<string>(?:L|u8|u|U)?"(?:[^"\\\n]|\\.)*")
  | (?P<char>(?:L|u8|u|U)?'(?:[^'\\\n]|\\.)*')
  | (?P<ident>[A-Za-z_]\w*)
  | (?P<number>\.?\d(?:[eEpP][+-]|[\w.])*)
  | (?P<punct>\.\.\.|<<=|>>=|->|\+\+|--|<<|>>|<=|>=|==|!=|&&|\|\||\#\#|::|[-+*/%&|^]=|[{}()\[\];,.?:~!%^&*+\-=<>|/\#])
  | (?P<other>\S)
''', re.VERBOSE | re.DOTALL)

OPEN_TO_CLOSE = {'(': ')', '[': ']', '{': '}'}
CLOSE_TO_OPEN = {v: k for k, v in OPEN_TO_CLOSE.items()}

AGGREGATE_KEYWORDS = ('struct', 'union', 'enum')

# Statements of the form MACRO(...); which don't declare anything.
NON_DECLARING_MACROS = ('C_ASSERT', 'static_assert', '_Static_assert', 'DEFINE_ENUM_FLAG_OPERATORS')

CPP_FUNCTION_QUALIFIERS = ('noexcept', 'const', 'volatile', 'override', 'final')


def tokenize(code: str, filename: str) -> List[Token]:
    """Tokenize C code. Each preprocessor directive becomes a single token."""
    tokens: List[Token] = []
    pos = 0
    line = 0
    line_start = 0
    at_line_start = True
    directive: Optional[Token] = None
    directive_start = 0

    while pos < len(code):
        if code.startswith('/*', pos) and code.find('*/', pos + 2) == -1:
            raise ParseError(f'{filename}:{line + 1}: unterminated block comment')

        match = TOKEN_REGEX.match(code, pos)
        assert match
        group = match.lastgroup
        assert group is not None
        text = match.group(0)
        token_line = line
        col = pos - line_start
        if '\n' in text:
            line += text.count('\n')
            line_start = pos + text.rindex('\n') + 1
        pos = match.end()

        if group == 'nl':
            if directive is not None:
                tokens.append(directive)
                directive = None
            at_line_start = True
            continue

        if group == 'ws':
            continue

        kind = TokenKind(group)
        token = Token(kind, text, token_line, line, col)

        if directive is not None:
            directive.text = code[directive_start:pos]
            directive.end_line = line
            if kind != TokenKind.COMMENT:
                directive.sub.append(token)
            continue

        if kind == TokenKind.OTHER:
            raise ParseError(f'{filename}:{token_line + 1}: unexpected character {text!r}')

        if kind == TokenKind.PUNCT and text == '#' and at_line_start:
            directive = Token(TokenKind.DIRECTIVE, text, token_line, line, col)
            directive_start = match.start()
            continue

        if kind != TokenKind.COMMENT:
            at_line_start = False
        tokens.append(token)

    if directive is not None:
        tokens.append(directive)

    return tokens


def is_annotation(name: str) -> bool:
    """Whether the identifier is an annotation or attribute macro, e.g. _In_ or DECLSPEC_ALIGN."""
    # Unlike all-caps names such as the _FOO_ struct tag, SAL names contain a lowercase letter.
    return ((re.fullmatch(r'_[A-Z]\w*_', name) is not None and not name.isupper()) or
            name.startswith('DECLSPEC_') or
            name in ('__declspec', '__attribute__', 'alignas', '_Alignas'))


def find_group_end(tokens: List[Token], start: int) -> int:
    """Return the index of the bracket which closes the one at tokens[start]."""
    depth = 0
    for i in range(start, len(tokens)):
        if tokens[i].kind != TokenKind.PUNCT:
            continue
        if tokens[i].text in OPEN_TO_CLOSE:
            depth += 1
        elif tokens[i].text in CLOSE_TO_OPEN:
            depth -= 1
            if depth == 0:
                return i
    raise ParseError(f'unclosed {tokens[start].text!r}')


def find_group_start(tokens: List[Token], end: int) -> int:
    """Return the index of the bracket which opens the one at tokens[end]."""
    depth = 0
    for i in range(end, -1, -1):
        if tokens[i].kind != TokenKind.PUNCT:
            continue
        if tokens[i].text in CLOSE_TO_OPEN:
            depth += 1
        elif tokens[i].text in OPEN_TO_CLOSE:
            depth -= 1
            if depth == 0:
                return i
    raise ParseError(f'unopened {tokens[end].text!r}')


def are_brackets_balanced(tokens: List[Token]) -> bool:
    stack: List[str] = []
    for token in tokens:
        if token.kind != TokenKind.PUNCT:
            continue
        if token.text in OPEN_TO_CLOSE:
            stack.append(token.text)
        elif token.text in CLOSE_TO_OPEN:
            if not stack or stack.pop() != CLOSE_TO_OPEN[token.text]:
                return False
    return not stack


def split_top_level(tokens: List[Token], separator: str) -> List[List[Token]]:
    parts: List[List[Token]] = [[]]
    depth = 0
    for token in tokens:
        if token.kind == TokenKind.PUNCT:
            if token.text in OPEN_TO_CLOSE:
                depth += 1
            elif token.text in CLOSE_TO_OPEN:
                depth -= 1
            elif token.text == separator and depth == 0:
                parts.append([])
                continue
        parts[-1].append(token)
    return parts


def is_aggregate_body(code: List[Token], brace: int) -> Optional[int]:
    """If code[brace] opens a struct/union/enum body, return the index of the keyword."""
    i = brace - 1

    # A parenthesized group right before the body is a function's parameter
    # list, unless it belongs to an attribute such as DECLSPEC_ALIGN(16).
    if i >= 0 and code[i].text == ')':
        start = find_group_start(code, i)
        if start == 0 or not is_annotation(code[start - 1].text):
            return None

    while i >= 0:
        token = code[i]
        if token.kind == TokenKind.IDENT:
            if token.text in AGGREGATE_KEYWORDS:
                return i
            i -= 1
        elif token.text == ':':
            i -= 1
        elif token.text == ')':
            i = find_group_start(code, i) - 1
        else:
            return None

    return None


class UnitKind(Enum):
    DIRECTIVE = auto()
    MARKER = auto()  # A // begin_xxx or // end_xxx comment.
    LINKAGE = auto()  # Opening or closing of an extern "C" block.
    STATEMENT = auto()


@dataclass
class Unit:
    kind: UnitKind
    tokens: List[Token]
    first_line: int
    last_line: int
    # For a statement unit, the statements on its lines.
    statements: List[List[Token]] = field(default_factory=list[List[Token]])


def group_units(tokens: List[Token], filename: str) -> List[Unit]:
    """Group tokens into directives, begin/end markers and top-level statements."""
    units: List[Unit] = []
    statement: List[Token] = []
    code: List[Token] = []  # The statement without comments and directives.
    brackets: List[Token] = []
    in_function_body = False
    linkage_depth = 0

    def close_statement():
        nonlocal statement, code, in_function_body
        # A lone ';' declares nothing.
        if len(code) > 1 or code[0].text != ';':
            units.append(Unit(UnitKind.STATEMENT, statement, code[0].line, statement[-1].end_line, [statement]))
        statement = []
        code = []
        in_function_body = False

    for token in tokens:
        if not code:
            if token.kind == TokenKind.COMMENT:
                if token.col == 0 and re.match(r'// (begin|end)_', token.text):
                    units.append(Unit(UnitKind.MARKER, [token], token.line, token.end_line))
                continue

            if token.kind == TokenKind.DIRECTIVE:
                units.append(Unit(UnitKind.DIRECTIVE, [token], token.line, token.end_line))
                continue

            if token.kind == TokenKind.IDENT and token.text in ('EXTERN_C_START', 'EXTERN_C_END'):
                units.append(Unit(UnitKind.LINKAGE, [token], token.line, token.end_line))
                continue

            if token.kind == TokenKind.PUNCT and token.text == '}' and linkage_depth > 0:
                linkage_depth -= 1
                units.append(Unit(UnitKind.LINKAGE, [token], token.line, token.end_line))
                continue

        is_pending_linkage = len(code) == 2 and code[0].text == 'extern' and code[1].kind == TokenKind.STRING

        if token.kind == TokenKind.DIRECTIVE and not brackets and not is_pending_linkage:
            raise ParseError(f'{filename}:{code[0].line + 1}: declaration is not terminated '
                             f'before the directive at line {token.line + 1}')

        statement.append(token)
        if token.kind in (TokenKind.COMMENT, TokenKind.DIRECTIVE):
            continue
        code.append(token)

        if token.kind != TokenKind.PUNCT:
            continue

        if token.text in OPEN_TO_CLOSE:
            if token.text == '{' and not brackets:
                if is_pending_linkage:
                    # extern "C" { ... } is transparent.
                    units.append(Unit(UnitKind.LINKAGE, statement, code[0].line, token.line))
                    for t in statement:
                        if t.kind == TokenKind.DIRECTIVE:
                            units.append(Unit(UnitKind.DIRECTIVE, [t], t.line, t.end_line))
                    linkage_depth += 1
                    statement = []
                    code = []
                    continue

                prev = code[-2] if len(code) > 1 else None
                if is_aggregate_body(code, len(code) - 1) is None and not (prev and prev.text == '='):
                    if not any(t.text == '(' for t in code):
                        raise ParseError(f'{filename}:{token.line + 1}: unexpected "{{"')
                    in_function_body = True

            brackets.append(token)
        elif token.text in CLOSE_TO_OPEN:
            if not brackets or OPEN_TO_CLOSE[brackets[-1].text] != token.text:
                raise ParseError(f'{filename}:{token.line + 1}: unexpected {token.text!r}')
            brackets.pop()
            if not brackets and in_function_body:
                close_statement()
        elif token.text == ';' and not brackets:
            close_statement()

    if code:
        raise ParseError(f'{filename}:{code[0].line + 1}: declaration is not terminated')
    if linkage_depth:
        raise ParseError(f'{filename}: extern "C" block is not terminated')

    units.sort(key=lambda u: u.first_line)

    # Chunks are made of whole lines, merge statements which share a line.
    merged: List[Unit] = []
    for unit in units:
        prev = merged[-1] if merged else None
        if (prev and prev.kind == UnitKind.STATEMENT and unit.kind == UnitKind.STATEMENT and
                unit.first_line <= prev.last_line):
            prev.tokens = prev.tokens + unit.tokens
            prev.statements = prev.statements + unit.statements
            prev.last_line = max(prev.last_line, unit.last_line)
            continue
        merged.append(unit)

    return merged


def declarator_name(tokens: List[Token]) -> str:
    """Return the name declared by a declarator, which may be preceded by specifiers."""
    tokens = split_top_level(tokens, '=')[0]

    # Trailing annotations and C++ qualifiers, e.g. "Foo(...) _Releases_lock_(x)".
    while tokens:
        last = tokens[-1]
        if last.text == ')':
            start = find_group_start(tokens, len(tokens) - 1)
            if start > 0 and (is_annotation(tokens[start - 1].text) or tokens[start - 1].text in ('noexcept', 'throw')):
                tokens = tokens[:start - 1]
                continue
        elif last.kind == TokenKind.IDENT and (is_annotation(last.text) or last.text in CPP_FUNCTION_QUALIFIERS):
            tokens = tokens[:-1]
            continue
        break

    def strip_arrays(tokens: List[Token]) -> List[Token]:
        while tokens and tokens[-1].text == ']':
            tokens = tokens[:find_group_start(tokens, len(tokens) - 1)]
        return tokens

    tokens = strip_arrays(tokens)
    if tokens and tokens[-1].text == ')':
        # Function parameters.
        tokens = strip_arrays(tokens[:find_group_start(tokens, len(tokens) - 1)])
        if tokens and tokens[-1].text == ')':
            # A parenthesized declarator, e.g. "(NTAPI *PFOO)".
            start = find_group_start(tokens, len(tokens) - 1)
            return declarator_name(tokens[start + 1:-1])

    if not tokens or tokens[-1].kind != TokenKind.IDENT:
        raise ParseError(f'no declarator name in: {" ".join(t.text for t in tokens)}')
    return tokens[-1].text


def get_statement_idents(statement: List[Token]) -> List[str]:
    code = [t for t in statement if t.kind not in (TokenKind.COMMENT, TokenKind.DIRECTIVE)]
    if code[-1].text == ';':
        code = code[:-1]

    # MACRO(Name, ...), e.g. DEFINE_GUID or DECLARE_HANDLE.
    if (code[0].kind == TokenKind.IDENT and len(code) > 1 and code[1].text == '(' and
            find_group_end(code, 1) == len(code) - 1):
        if code[0].text in NON_DECLARING_MACROS:
            return []
        first_arg = split_top_level(code[2:-1], ',')[0]
        if len(first_arg) != 1 or first_arg[0].kind != TokenKind.IDENT:
            raise ParseError(f'unsupported macro statement {code[0].text}')
        return [first_arg[0].text]

    # struct X; or enum X;
    if len(code) == 2 and code[0].text in AGGREGATE_KEYWORDS and code[1].kind == TokenKind.IDENT:
        return [code[1].text]

    is_typedef = any(t.text == 'typedef' for t in code)

    brace = next((i for i, t in enumerate(code) if t.text == '{'), None)
    if brace is not None and code[brace - 1].text != '=':
        keyword = is_aggregate_body(code, brace)
        if keyword is None:
            # Function definition.
            return [declarator_name(code[:brace])]

        if not is_typedef:
            raise ParseError(f'{code[keyword].text} definition without typedef')

        # The tag directly precedes the body, anything before it is an attribute.
        tag = None
        i = keyword + 1
        while i < brace and code[i].text != ':':
            if code[i].text == '(':
                i = find_group_end(code, i) + 1
                continue
            is_macro_call = i + 1 < brace and code[i + 1].text == '('
            if code[i].kind == TokenKind.IDENT and not is_macro_call and not is_annotation(code[i].text):
                tag = code[i].text
            i += 1

        body_end = find_group_end(code, brace)
        names = [declarator_name(d) for d in split_top_level(code[body_end + 1:], ',')]
        return names + ([f'{code[keyword].text} {tag}'] if tag else [])

    names = [declarator_name(d) for d in split_top_level(code, ',')]

    if is_typedef:
        # typedef struct _X X, *PX;
        i = next(i for i, t in enumerate(code) if t.text == 'typedef') + 1
        if i + 1 < len(code) and code[i].text in AGGREGATE_KEYWORDS and code[i + 1].kind == TokenKind.IDENT:
            names.append(f'{code[i].text} {code[i + 1].text}')

        # Use the routine name for typedefs of functions loaded at runtime.
        comment = next((t for t in statement if t.kind == TokenKind.COMMENT and t.line == code[0].line), None)
        if comment and (match := re.fullmatch(r'//\s+routine:\s+(\w+)( \(.*\))?', comment.text)):
            if len(names) != 1:
                raise ParseError(f'routine comment for multiple names: {names}')
            names = [match.group(1)]

    return names


def get_directive_idents(directive: Token) -> List[str]:
    sub = directive.sub
    if len(sub) < 2 or sub[0].text != 'define':
        return []

    name = sub[1].text
    if name.startswith('PHNT_'):
        return []

    # Defined without a value.
    if len(sub) == 2:
        return []

    return [name]


def read_header(path: Path) -> str:
    """Read a header, normalized for parsing. Line numbers are preserved."""
    code = path.read_text()
    original_newline_count = code.count('\n')

    # Tabs to spaces, only at the beginning of the line.
    code = re.sub(r'^\t+', lambda x: 4 * ' ' * len(x.group(0)), code, flags=re.MULTILINE)

    def blank(match: re.Match[str]) -> str:
        return re.sub(r'[^\n]', '', match.group(0))

    # Remove the block comment at the top of the file.
    code = re.sub(r'^/\*.*?\*/', blank, code, flags=re.DOTALL)

    # Remove the C++ helpers of RTL_CONSTANT_STRING.
    code = re.sub(
        r'^#ifdef __cplusplus\nextern "C\+\+"\n\{\ntemplate <size_t N> char _RTL_CONSTANT_STRING_type_check\b.*?^#endif\n',
        blank,
        code,
        flags=re.DOTALL | re.MULTILINE,
    )

    assert code.count('\n') == original_newline_count
    return code


class ScopeKind(Enum):
    IF = auto()
    MARKER = auto()
    PACK = auto()


@dataclass
class Scope:
    kind: ScopeKind
    line_number: int
    text: str  # The first line of the code which opens the scope.


def split_header_to_chunks(path: Path, origin: ChunkOrigin = ChunkOrigin.PHNT) -> List[Chunk]:
    code = read_header(path)
    units = group_units(tokenize(code, path.name), path.name)

    lines = code.split('\n')
    lines = [x + '\n' for x in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

    result: List[Chunk] = []
    before: List[Tuple[str, str]] = []
    after: List[str] = []
    scopes: List[Scope] = []

    def open_scope(kind: ScopeKind, intro: str, body: str, end: str, line_number: int):
        before.append((intro, body))
        after.insert(0, end)
        scopes.append(Scope(kind, line_number, body.strip().splitlines()[0]))

    def check_scope(kind: ScopeKind, line_number: int, body: str):
        if scopes and scopes[-1].kind == kind:
            return
        text = body.strip().splitlines()[0]
        if not scopes:
            raise ParseError(f'{path.name}:{line_number}: "{text}" has nothing to match')
        raise ParseError(f'{path.name}:{line_number}: "{text}" does not match "{scopes[-1].text}" at line {scopes[-1].line_number}')

    def close_scope(kind: ScopeKind, line_number: int, body: str):
        check_scope(kind, line_number, body)
        before.pop()
        after.pop(0)
        scopes.pop()

    last_line = -1
    for unit in units:
        intro = ''
        for line in lines[last_line + 1:unit.first_line]:
            if intro == '' and line.strip() == '':
                continue
            intro += line

        body = ''.join(lines[unit.first_line:unit.last_line + 1])
        last_line = max(last_line, unit.last_line)
        line_number = unit.first_line + 1

        if unit.kind == UnitKind.LINKAGE:
            continue

        if unit.kind == UnitKind.MARKER:
            if body.startswith('// begin_'):
                open_scope(ScopeKind.MARKER, intro, body, re.sub(r'^// begin_(\w+).*$', r'// end_\1', body), line_number)
            else:
                close_scope(ScopeKind.MARKER, line_number, body)
            continue

        if unit.kind == UnitKind.DIRECTIVE:
            directive = unit.tokens[0]
            name = directive.sub[0].text if directive.sub else ''

            if name in ('if', 'ifdef', 'ifndef'):
                open_scope(ScopeKind.IF, intro, body, '#endif\n', line_number)
                continue

            if name in ('else', 'elif'):
                check_scope(ScopeKind.IF, line_number, body)
                popped_intro, popped_body = before.pop()
                before.append((popped_intro, popped_body + '// ...\n' + body))
                continue

            if name == 'endif':
                close_scope(ScopeKind.IF, line_number, body)
                continue

            if name == 'include':
                include = ''.join(t.text for t in directive.sub[1:]).strip('<>"')
                if re.fullmatch(r'pshpack\d+\.h', include):
                    open_scope(ScopeKind.PACK, intro, body, '#include <poppack.h>\n', line_number)
                    continue
                if include == 'poppack.h':
                    close_scope(ScopeKind.PACK, line_number, body)
                    continue

            idents = get_directive_idents(directive)
        else:
            try:
                idents = [ident for statement in unit.statements for ident in get_statement_idents(statement)]
            except ParseError as e:
                raise ParseError(f'{path.name}:{line_number}: {e}\n{body}') from e

        if len(idents) == 0:
            continue

        result.append(Chunk(
            origin=origin,
            code_url=f'{path.name}#L{line_number}',
            idents=idents,
            before=list(before),
            intro=intro,
            body=body,
            after=list(after),
        ))

    if scopes:
        raise ParseError(f'{path.name}:{scopes[-1].line_number}: "{scopes[-1].text}" is not closed')

    return result


def lint_header(path: Path) -> List[str]:
    """Return warnings about code which compiles but is likely a mistake."""
    code = read_header(path)
    lines = code.split('\n')
    warnings: List[str] = []

    for token in tokenize(code, path.name):
        if token.kind != TokenKind.DIRECTIVE or not token.sub:
            continue

        location = f'{path.name}:{token.line + 1}'

        if lines[token.end_line].rstrip().endswith('\\'):
            warnings.append(f'{location}: line continuation at the end of the directive')

        for prev, t in zip(token.sub, token.sub[1:]):
            if prev.text == '#' and lines[prev.line][:prev.col].strip() == '' and t.text in (
                    'define', 'undef', 'if', 'ifdef', 'ifndef', 'elif', 'else', 'endif', 'include', 'pragma'):
                warnings.append(f'{location}: line continuation pulls the directive at line {prev.line + 1} into it')

        if token.sub[0].text in ('define', 'if', 'elif') and not are_brackets_balanced(token.sub[1:]):
            warnings.append(f'{location}: unbalanced brackets')

    return warnings

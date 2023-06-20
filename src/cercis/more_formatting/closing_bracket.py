import ast
from collections import defaultdict
from typing import Dict, List, Set

from tokenize_rt import Token, src_to_tokens, tokens_to_src


def collapse_closing_paren_in_func_call(src: str) -> str:
    """
    This function will reformat this:

    print(
        'hiiiiiiiiii',
        'thereeeeee',
    )

    into this:

    print(
        'hiiiiiiiiii',
        'thereeeeee')
    """
    tokens_to_fix: Set[Token] = set()
    tree = ast.parse(source=src)
    all_tokens = src_to_tokens(src)
    tokens_lookup = _organize_tokens_by_line(all_tokens)
    _collect_tokens_to_fix(tree, tokens_lookup, tokens_to_fix)
    _fix_tokens(tokens_lookup, tokens_to_fix)
    fixed_tokens = _rearrange_tokens(tokens_lookup)
    return tokens_to_src(fixed_tokens)  # type: ignore[no-any-return]


def _collect_tokens_to_fix(
        tree: ast.Module,
        tokens_lookup: Dict[int, List[Token]],
        tokens_to_fix: Set[Token],
) -> None:
    """Only when a line has only `)\n` do we consider fixing it"""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if node.end_lineno not in tokens_lookup:  # type: ignore[attr-defined]
                pass
            else:
                tokens_this_line = tokens_lookup[node.end_lineno]  # type: ignore[attr-defined]

                if _eligible_for_fixing(tokens_this_line):
                    tokens_to_fix.add(tokens_this_line[-2])


def _eligible_for_fixing(tokens: List[Token]) -> bool:
    if len(tokens) < 2:
        return False

    if len(tokens) == 2:
        return _is_right_paren(tokens[0]) and _is_newline(tokens[1])

    for token in tokens[:-2]:
        if token.name != 'UNIMPORTANT_WS':
            return False

    return _is_right_paren(tokens[-2]) and _is_newline(tokens[-1])


def _fix_tokens(
        tokens_lookup: Dict[int, List[Token]],
        tokens_to_fix: Set[Token],
) -> None:
    for token in tokens_to_fix:
        prev_line = token.line - 1
        if prev_line in tokens_lookup:
            prev_line_tokens: List[Token] = tokens_lookup[prev_line]
            newline: Token = prev_line_tokens[-1]
            last_2_col_offset: int = prev_line_tokens[-2].utf8_byte_offset

            if _is_comma(prev_line_tokens[-2]):
                paren = Token(
                    name='OP',
                    src=')',
                    line=prev_line,
                    utf8_byte_offset=last_2_col_offset,
                )
                new_tokens = prev_line_tokens[:-2] + [paren] + [newline]
            else:
                paren = Token(
                    name='OP',
                    src=')',
                    line=prev_line,
                    utf8_byte_offset=last_2_col_offset + 1,
                )
                mod_newline = Token(
                    name=newline.name,
                    src=newline.src,
                    line=newline.line,
                    utf8_byte_offset=newline.utf8_byte_offset + 1,
                )
                new_tokens = prev_line_tokens[:-1] + [paren] + [mod_newline]

            tokens_lookup[prev_line] = new_tokens
            tokens_lookup.pop(token.line)  # ditch the line of `)\n`


def _organize_tokens_by_line(tokens: List[Token]) -> Dict[int, List[Token]]:
    result = defaultdict(list)
    for token in tokens:
        result[token.line].append(token)

    return result


def _rearrange_tokens(tokens_lookup: Dict[int, List[Token]]) -> List[Token]:
    result = []
    for _, tokens_this_line in tokens_lookup.items():
        result.extend(tokens_this_line)

    return result


def _is_right_paren(token: Token) -> bool:
    return token.name == 'OP' and token.src == ')'  # type: ignore[no-any-return]


def _is_newline(token: Token) -> bool:
    return token.name == 'NEWLINE' and token.src == '\n'  # type: ignore[no-any-return]


def _is_comma(token: Token) -> bool:
    return token.name == 'OP' and token.src == ','  # type: ignore[no-any-return]

from cercis.mode import Mode
from cercis.more_formatting.closing_paren import collapse_closing_paren_in_func_call


def format_more(src: str, mode: Mode) -> str:
    if mode.collapse_closing_paren_in_function_call:
        src = collapse_closing_paren_in_func_call(src)

    return src

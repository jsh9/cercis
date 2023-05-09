from enum import Enum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cercis import Mode

SPACE: str = " "
TAB: str = "\t"
TWO_TABS: str = "\t\t"


class Indent(Enum):
    DEDENT = auto()
    BLOCK = auto()
    FUNCTION_DEF_CONTINUATION = auto()
    OTHER_LINE_CONTINUATION = auto()

    def get_indent_chars(self, mode: "Mode") -> str:
        if self == Indent.DEDENT:
            raise ValueError("Internal error: this method is invalid for DEDENT")

        if mode.use_tabs:
            if self == Indent.OTHER_LINE_CONTINUATION:
                return TWO_TABS if mode.other_line_continuation_extra_indent else TAB

            if self == Indent.FUNCTION_DEF_CONTINUATION:
                return TWO_TABS if mode.function_definition_extra_indent else TAB

            return TAB

        spaces = SPACE * mode.base_indent_level
        if self == Indent.OTHER_LINE_CONTINUATION:
            return spaces * 2 if mode.other_line_continuation_extra_indent else spaces

        if self == Indent.FUNCTION_DEF_CONTINUATION:
            return spaces * 2 if mode.function_definition_extra_indent else spaces

        return spaces

from enum import Enum, auto
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from cercis import Mode

SPACE: str = " "
TAB: str = "\t"
TWO_TABS: str = "\t\t"


class Indent(Enum):
    """
    A class to hold different indentation types.

    Here is a brief explanation of the 4 types:
        - Dedent: It's actually the opposite of "indent"; we put it here
                  just because we'd like for all indent/dedent types to
                  be in the same place
        - Block: The indentation that should happen within a code block
                 (such as in a class, a function, a for loop, an if loop, ...)
        - Function definition continuation:
                When the "def function_name(...)" becomes too long, we wrap
                the list of arguments in new lines. This is one type of line
                continuation, which corresponds to this type of indentation.
        - Other line continuation:
                Other types of line continuation, such as when
                result = my_function(1, 2, 3, 4, 5, ...) becomes too long
                and we have to wrap this line. The corresponding indentation
                falls under this type.
    """
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


class IndentCharacters:
    """
    A class to hold characters (spaces or tabs).

    Attributes:
        indents:
            A collection of indents on a particular line of code
        mode:
            Contains information to determine how to render the indents
            into actual characters, or how to calculate the length of
            the indents
    """
    def __init__(self, indents: Tuple[Indent, ...], mode: "Mode") -> None:
        self.indents = indents
        self.mode = mode

    def render(self) -> str:
        """Render the indents as actual characters"""
        return "".join(_.get_indent_chars(self.mode) for _ in self.indents)

    def calc_total_width(self) -> int:
        """Calculate the width of all the indents. We are not using len()
        because we can't simply consider a tab ('\t') to have width 1
        when rendering."""
        TAB_DISPLAYING_WIDTH = 4
        spaces_for_tab = " " * TAB_DISPLAYING_WIDTH
        chars_to_render: str = self.render().replace(TAB, spaces_for_tab)
        return len(chars_to_render)

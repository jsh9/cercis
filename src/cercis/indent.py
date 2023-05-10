from enum import Enum, auto
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from cercis import Mode

SPACE: str = " "
TAB: str = "\t"
TWO_TABS: str = "\t\t"


class Indent(Enum):
    """
    A class to represent an indentation, which can belong to 1 of 4 types.

    Here is a brief explanation of these 4 types:
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

    The implementation of this class is inspired by a similar implementation
    in Pyink -- in particular, here: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/src/pyink/lines.py#L52-L61  # noqa: B950

    Pyink is a formatter that forks from Black. It inherits Black's MIT license.
    """

    DEDENT = auto()
    BLOCK = auto()
    FUNCTION_DEF_CONTINUATION = auto()
    OTHER_LINE_CONTINUATION = auto()

    def render(
            self,
            mode: "Mode",
            for_width_calculation: bool = False,
    ) -> str:
        """Render this indentation into actual characters.

        Args:
            mode:
                The global configuration of Cercis
            for_width_calculation:
                If True, we are rendering this indentation to calculate the
                width of the current line (if width > length limit, wrap line).
                If False, we are rendering this indentation to be included
                in the result.
        """
        if self == Indent.DEDENT:
            raise ValueError("Internal error: this method is invalid for DEDENT")

        if mode.use_tabs:
            if self == Indent.OTHER_LINE_CONTINUATION:
                ch = TWO_TABS if mode.other_line_continuation_extra_indent else TAB
            elif self == Indent.FUNCTION_DEF_CONTINUATION:
                ch = TWO_TABS if mode.function_definition_extra_indent else TAB
            else:
                ch = TAB

            if not for_width_calculation:
                return ch

            spaces_for_one_tab = " " * mode.tab_width
            return ch.replace(TAB, spaces_for_one_tab)

        spaces = SPACE * mode.base_indentation_spaces
        if self == Indent.OTHER_LINE_CONTINUATION:
            return spaces * 2 if mode.other_line_continuation_extra_indent else spaces

        if self == Indent.FUNCTION_DEF_CONTINUATION:
            return spaces * 2 if mode.function_definition_extra_indent else spaces

        return spaces


class MultipleIndents:
    """
    A class to hold multiple indentations.

    Attributes:
        indents:
            A collection of indents on a particular line of code
        mode:
            Global configuration, which contains information to determine
            how to render the indents into actual characters, or how to
            calculate the width of the indents
    """

    def __init__(self, indents: Tuple[Indent, ...], mode: "Mode") -> None:
        self.indents = indents
        self.mode = mode

    def render(self, for_width_calculation: bool = False) -> str:
        """Render the indents as actual characters.

        Args:
            for_width_calculation:
                If True, we are rendering this indentation to calculate the
                width of the current line (if width > length limit, wrap line).
                If False, we are rendering this indentation to be included
                in the formatting output.
        """
        return "".join(_.render(self.mode, for_width_calculation) for _ in self.indents)

    def calc_total_width(self) -> int:
        """Calculate the width of all the indents. We are not using len()
        because we can't simply treat a tab ('\t') as width 1
        when rendering."""
        chars_to_render: str = self.render(for_width_calculation=True)
        return len(chars_to_render)

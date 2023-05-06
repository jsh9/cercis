from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, List, Optional, Type

from blib2to3.pgen2 import token
from blib2to3.pytree import Leaf
from cercis.lines import Line
from cercis.nodes import CLOSING_BRACKETS, OPENING_BRACKETS

if TYPE_CHECKING:
    from cercis.linegen import _BracketSplitComponent
    from cercis.mode import Mode


@dataclass
class CollapseNestedBracketsReturnValues:
    head_leaves: List[Leaf]
    body_leaves: List[Leaf]
    tail_leaves: List[Leaf]
    body: Optional[Line]


def perform_collapse_nested_brackets(
        *,
        line: Line,
        opening_bracket: Leaf,
        closing_bracket: Leaf,
        head_leaves: List[Leaf],
        body_leaves: List[Leaf],
        tail_leaves: List[Leaf],
        mode: "Mode",
        bracket_split_build_line_func: Callable[..., Line],
        bracket_split_component: "Type[_BracketSplitComponent]",
) -> CollapseNestedBracketsReturnValues:
    """
    The code of this function comes from a wonderful implementation
    from another Black fork: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/src/pyink/linegen.py#L778-L815  # noqa: B950

    Pyink inherits the license of Black, which is already included in this
    repo (the file OLD_LICENSE).
    """
    opening_brackets: List[Leaf] = [opening_bracket]
    body: Optional[Line] = None
    if mode.collapse_nested_brackets and not (
        # Only look inside when it doesn't start with invisible parens.
        opening_bracket.type == token.LPAR
        and not opening_bracket.value
        and closing_bracket.type == token.RPAR
        and not closing_bracket.value
    ):
        # Find an inner body...
        inner_body_leaves = list(body_leaves)
        inner_opening_brackets: List[Leaf] = []
        inner_closing_brackets: List[Leaf] = []
        while (
            len(inner_body_leaves) >= 2
            and inner_body_leaves[0].type in OPENING_BRACKETS
            and inner_body_leaves[-1].type in CLOSING_BRACKETS
            and inner_body_leaves[-1].opening_bracket is inner_body_leaves[0]
        ):
            inner_opening_brackets.append(inner_body_leaves.pop(0))
            inner_closing_brackets.insert(0, inner_body_leaves.pop())
        if len(inner_body_leaves) < len(body_leaves):
            inner_body = bracket_split_build_line_func(
                inner_body_leaves,
                line,
                opening_brackets[0],
                component=bracket_split_component.body,
                mode=mode,
            )
            if inner_body.should_split_rhs or (
                inner_body_leaves and inner_body_leaves[-1].type == token.COMMA
            ):
                # Only when the inner body itself will be split or ends with a comma,
                # should we prefer not break immediately nested brackets.
                body_leaves = inner_body_leaves
                head_leaves.extend(inner_opening_brackets)
                tail_leaves = inner_closing_brackets + tail_leaves
                body = inner_body  # No need to re-calculate body.

    return CollapseNestedBracketsReturnValues(
        head_leaves=head_leaves,
        body_leaves=body_leaves,
        tail_leaves=tail_leaves,
        body=body,
    )

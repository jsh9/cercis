from typing import List

from blib2to3.pgen2 import token
from blib2to3.pytree import Leaf
from cercis.lines import Line


def check_eligibility_to_opt_out_of_line_wrapping(
        line: Line,
        wrap_line_with_long_string: bool,
) -> bool:
    """
    Only "simple" lines are eligible for opting out of line wrapping.

    Some examples of "simple" lines:
        - var = "yes"
        - var = "hello"     " world"
        - var = "very very very very very very very very very long string"
        - var.attr.c.d = "very very very very very very very very long string"

    The last element of the line, except for the comment, must be a string.

    Some examples of "non-simple" lines:
        - var = "hello" + "world"
        - lookUp["key"] = "hello world"

    For a more comprehensive list of examples, go to `test_lingen.py` and
    check out the test cases.
    """
    if wrap_line_with_long_string:  # comes from top-level config
        return False  # not eligible (always use Black's default behavior)

    if len(line.comments) > 0:
        # As long as there are any comments, we don't consider this `line`
        # eligible for opting out, i.e., we fall back to Black's default
        # behaviors.
        #
        # If we don't fall back, there will be conflicts with Black's
        # experimental features ("--preview").
        return False

    if len(line.leaves) == 0:
        return False

    # LPAR and RPAR are added during node visiting (in `lines.visit(src_node)`)
    if line.leaves[-1].type == token.RPAR:
        leaves = _clone_leaves(line.leaves[:-1])
        has_rpar = True
    else:
        leaves = _clone_leaves(line.leaves)
        has_rpar = False

    if len(leaves) == 0 or not _is_string(leaves[-1]):
        return False

    while len(leaves) > 0:  # check leaf by leaf from right hand side
        leaves = leaves[:-1]
        if len(leaves) == 0:
            break  # note: all([]) is True

        if _is_string(leaves[-1]):
            continue

        if has_rpar and leaves[-1].type == token.LPAR:
            has_rpar = False
            continue

        if not _is_equal_operators(leaves[-1]):
            return False

        leaves = leaves[:-1]
        break

    return all(_is_name_or_dot(_) for _ in leaves)


def _clone_leaves(leaves: List[Leaf]) -> List[Leaf]:
    return [_.clone() for _ in leaves]


def _is_string(leaf: Leaf) -> bool:
    return leaf.type == token.STRING


def _is_equal_operators(leaf: Leaf) -> bool:
    if leaf.type == token.EQUAL:
        return True

    return 37 <= leaf.type <= 47


def _is_name_or_dot(leaf: Leaf) -> bool:
    return leaf.type in {token.NAME, token.DOT}

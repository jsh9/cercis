import pytest

import cercis
from cercis.utils_line_wrapping import check_eligibility_to_opt_out_of_line_wrapping

str1 = 'variable = "very very very very very very very very very very very very very very long string"'  # noqa: B950
str2 = 'some_class.a.b.some_variable_name = ("Once upon a time there is"  " a village alongside the river that flows quitely.")'  # noqa: B950


@pytest.mark.parametrize(
    "src_in, expected",
    [
        ("a = 2", False),
        ('a = "hello"', True),
        ("a = 'hello'", True),
        ('a = ("hello")', True),
        ('a = (("hello"))', True),
        ('a = ((("hello")))', True),
        ('a = (((((((((("hello"))))))))))', True),
        ('a = (((((((((("hello"))))))))), )', False),
        ('a = ("hello") ("world") ("good") ("morning")', False),
        ('a = "hello" + "world"', False),
        ('a = "hello""world"', True),
        ('a = "hello" "world"', True),
        ('a = "hello", "world"', False),
        ('a = "hello"  "world"', True),
        ('a = "hello"\t"world"', True),
        ('a = "hello" \t \t "world"', True),
        ('a = "hello" "world" "hello" "world" "hello"\t"world"  "hello"', True),
        ('a["key"].field[0] = "hello"', False),
        ('a[-1] = "hello"', False),
        ('func(thing) = "hello"', False),
        ('a.get("key") = "hello"', False),
        ('a.b.c.d.e.f.g.h.i.j.k.l.m.n = "hello"', True),
        ('a.b.c.d.e.f.g.h.i.j.k.l.m.n[0] = "hello"', False),
        ('a.b.c.d.e.f.g.h.i.j.k.l.m.n() = "hello"', False),
        ('a.b.c.d.e.f.g.h.i.j.k.l.m.n.__str__ = "hello"', True),
        (str1, True),
        (str2, True),
        ('"a string"', True),
        ('("another string")', True),
        ('(("a third string"))', False),
        ('(("a third string", ), )', False),
        ("12345678901234567890123456789012345678901234567890", False),
        ("3.14159265358979323846", False),
        ("pi = 3.14159265358979323846", False),
        ("pi = '3.14159265358979323846'", True),
        ('a = "hello",', False),
    ],
)
def test_check_line_eligibility_to_opt_out_of_line_wrapping(
        src_in: str,
        expected: bool,
) -> None:
    mode = cercis.Mode()
    src_node = cercis.lib2to3_parse(src_in.lstrip(), mode.target_versions)
    line_generator = cercis.LineGenerator(mode=mode, features=[])
    lines = list(line_generator.visit(src_node))
    assert len(lines) == 1

    eligible = check_eligibility_to_opt_out_of_line_wrapping(
        lines[0],
        wrap_line_with_long_string=False,
    )
    assert eligible == expected

long_unmergable_string_with_pragma = (
    "This is a really long string that can't be merged because it has a likely pragma at the end"  # type: ignore
    " of it."
)

long_unmergable_string_with_pragma = (
    "This is a really long string that can't be merged because it has a likely pragma at the end"  # noqa
    " of it."
)

long_unmergable_string_with_pragma = (
    "This is a really long string that can't be merged because it has a likely pragma at the end"  # pylint: disable=some-pylint-check
    " of it."
)

long_unmergable_string_with_comment = (
    "This is a really long string that can't be merged because it has a likely pragma at the end"  # hello world
    " of it."
)

long_unmergable_string_with_comment = (
    "This is a really long string that can't be merged because it has a likely pragma at the end"
    " of it."  # good morning
)

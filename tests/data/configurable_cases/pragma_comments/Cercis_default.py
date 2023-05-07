# Some test cases in this file comes from: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/tests/data/pyink/pragma_comments.py
a_very_long_library_name._private_method(and_a_long_arg)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint:disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint: disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint:  disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pytype:disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pytype: disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pytype:  disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # noqa:E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # noqa: E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # noqa:  E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type:ignore[something]

a_very_long_library_name._private_method(and_a_long_arg)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type: ignore[something]

a_very_long_library_name._private_method(and_a_long_arg)  # type:  ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type:  ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type:  ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type:  ignore[something]

# output

# Some test cases in this file comes from: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/tests/data/pyink/pragma_comments.py
a_very_long_library_name._private_method(and_a_long_arg)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint:disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint:disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint: disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint: disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint:  disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint:  disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype:disable=attribute-error
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pytype:disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype: disable=attribute-error
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pytype: disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pytype:  disable=attribute-error
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pytype:  disable=attribute-error

a_very_long_library_name._private_method(and_a_long_arg)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # noqa:E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # noqa: E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa:  E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # noqa:  E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type:ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # type:ignore[something]

a_very_long_library_name._private_method(and_a_long_arg)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type: ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # type: ignore[something]

a_very_long_library_name._private_method(and_a_long_arg)  # type:  ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type:  ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type:  ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # type:  ignore[something]

# Some test cases in this file comes from: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/tests/data/pyink/pragma_comments.py
a_very_long_library_name._private_method(and_a_long_arg)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint: disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint:disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint:disable=protected-access

a_very_long_library_name._private_method(and_a_long_arg)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # noqa: E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(and_a_long_arg)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # noqa:E123, W234, ABC456, XYZ2

# Black does not wrap a line, no matter how long,
# if it has "# type: ignore" at the end.
a_very_long_library_name._private_method(and_a_long_arg)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type: ignore[something]
a_very_long_library_name._private_method(Though_hundreds_of_thousands_had_done_their_very_best_to_disfigure_the_small_piece_of_land_on_which_they_were_crowded_together_by_paving_the_ground_with_stones_scraping_away_every_vestige_of_vegetation_cutting_down_the_trees_turning_away_birds_and_beasts_and_filling_the_air_with_the_smoke_of_naphtha_and_coal_still_spring_was_spring_even_in_the_town)  # type: ignore[something]

# Black only exempts "# type: ignore" but not "# type:ignore".
# The latter is also valid for mypy and many people use the latter.
a_very_long_library_name._private_method(and_a_long_arg)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type:ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type:ignore[something]
a_very_long_library_name._private_method(Though_hundreds_of_thousands_had_done_their_very_best_to_disfigure_the_small_piece_of_land_on_which_they_were_crowded_together_by_paving_the_ground_with_stones_scraping_away_every_vestige_of_vegetation_cutting_down_the_trees_turning_away_birds_and_beasts_and_filling_the_air_with_the_smoke_of_naphtha_and_coal_still_spring_was_spring_even_in_the_town)  # type:ignore[something]

# output

# Some test cases in this file comes from: https://github.com/google/pyink/blob/f93771c02e9a26ce9508c59d69c9337c95797eac/tests/data/pyink/pragma_comments.py
a_very_long_library_name._private_method(
    and_a_long_arg
)  # pylint: disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit_
)  # pylint: disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit___
)  # pylint: disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint: disable=protected-access

a_very_long_library_name._private_method(
    and_a_long_arg
)  # pylint:disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit_
)  # pylint:disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit___
)  # pylint:disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint:disable=protected-access

a_very_long_library_name._private_method(
    and_a_long_arg
)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit_
)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit___
)  # noqa: E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # noqa: E123, W234, ABC456, XYZ2

a_very_long_library_name._private_method(
    and_a_long_arg
)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit_
)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit___
)  # noqa:E123, W234, ABC456, XYZ2
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # noqa:E123, W234, ABC456, XYZ2

# Black does not wrap a line, no matter how long,
# if it has "# type: ignore" at the end.
a_very_long_library_name._private_method(and_a_long_arg)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # type: ignore[something]
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # type: ignore[something]
a_very_long_library_name._private_method(Though_hundreds_of_thousands_had_done_their_very_best_to_disfigure_the_small_piece_of_land_on_which_they_were_crowded_together_by_paving_the_ground_with_stones_scraping_away_every_vestige_of_vegetation_cutting_down_the_trees_turning_away_birds_and_beasts_and_filling_the_air_with_the_smoke_of_naphtha_and_coal_still_spring_was_spring_even_in_the_town)  # type: ignore[something]

# Black only exempts "# type: ignore" but not "# type:ignore".
# The latter is also valid for mypy and many people use the latter.
a_very_long_library_name._private_method(
    and_a_long_arg
)  # type:ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit_
)  # type:ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_just_fits_limit___
)  # type:ignore[something]
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # type:ignore[something]
a_very_long_library_name._private_method(
    Though_hundreds_of_thousands_had_done_their_very_best_to_disfigure_the_small_piece_of_land_on_which_they_were_crowded_together_by_paving_the_ground_with_stones_scraping_away_every_vestige_of_vegetation_cutting_down_the_trees_turning_away_birds_and_beasts_and_filling_the_air_with_the_smoke_of_naphtha_and_coal_still_spring_was_spring_even_in_the_town
)  # type:ignore[something]

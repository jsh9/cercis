# These test cases demonstrate how line length calculation changes when
# we assign different widths to one tab. When tab width is small, some lines
# do not exceed the length limit. And when we increase tab width, the same
# lines start to exceed the limit and get wrapped.
if True:
	results = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15

	result = some_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 90)

	class ClassWithLongName(ParentClassWithLongNameA, ParentClassWithLongNameB_):
		def __init__(self):
			pass

	def inner_func_with_very_long_name(arg1_with_longname, arg_2_with_long_name_):
		pass

	result = inner_func_with_very_long_name(123456789123456789, 'abcdefghijklmnop')


# output

# These test cases demonstrate how line length calculation changes when
# we assign different widths to one tab. When tab width is small, some lines
# do not exceed the length limit. And when we increase tab width, the same
# lines start to exceed the limit and get wrapped.
if True:
	results = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15

	result = some_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 90)

	class ClassWithLongName(ParentClassWithLongNameA, ParentClassWithLongNameB_):
		def __init__(self):
			pass

	def inner_func_with_very_long_name(arg1_with_longname, arg_2_with_long_name_):
		pass

	result = inner_func_with_very_long_name(
		123456789123456789, 'abcdefghijklmnop'
	)

"""The test cases in this file comes from https://github.com/google/pyink,
which inherits Black's license (MIT license).
"""

# Literal list/tuple/set/dict will always be exploded on their own, immediately
# nested brackets should match this behavior.
literal_inner_set = [{
    1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012
}]

literal_inner_list = [[
    1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012
]]

literal_inner_tuple = [(
    1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012
)]

literal_inner_dict = [{
    1001: 1002, 1003: 1004, 1005: 1006, 1007: 1008, 1009: 1010, 1011: 1012
}]

literal_inner_multiple = [[[
    1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012
]]]


# Make sure trailing comma is still handled correctly.
some_var = [
    some_module_name.SomeClassName(arg_one="value_one", arg_two="value_two"),
    some_module_name.SomeClassName(arg_one="value_one", arg_two="value_two")
]


# output

"""The test cases in this file comes from https://github.com/google/pyink,
which inherits Black's license (MIT license).
"""

# Literal list/tuple/set/dict will always be exploded on their own, immediately
# nested brackets should match this behavior.
literal_inner_set = [
    {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012}
]

literal_inner_list = [
    [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012]
]

literal_inner_tuple = [
    (1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012)
]

literal_inner_dict = [
    {1001: 1002, 1003: 1004, 1005: 1006, 1007: 1008, 1009: 1010, 1011: 1012}
]

literal_inner_multiple = [
    [[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012]]
]


# Make sure trailing comma is still handled correctly.
some_var = [
    some_module_name.SomeClassName(arg_one="value_one", arg_two="value_two"),
    some_module_name.SomeClassName(arg_one="value_one", arg_two="value_two"),
]

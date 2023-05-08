# Line length limit: 30 chars,
# which is right here:       |


def function(arg1: int,
             arg2: float,
             arg3_with_very_long_name: list):
    print('Hello world')


def func2(arg1: int,
          arg2: float,
          arg3_with_very_long_name: list) -> None:
    print('Hello world')


result = func2(12345, 3.1415926, [1, 2, 3])

result = [123, 456, 789, -123, -456]

something = {'a': 1, 'b': 2, 'c': 3}

some_tuple = (1, 2, 3, 4, 5, 6, 7, 8)


class A:
    def __init__(self, a, b, c, d):
        print('hello world')


class B:
    def __init__(self, a, b, c, d,):
        print('hello world')


# Line length limit: 30 chars,
# which is right here:       |


# output


# Line length limit: 30 chars,
# which is right here:       |


def function(
        arg1: int,
        arg2: float,
        arg3_with_very_long_name: list,
):
    print('Hello world')


def func2(
        arg1: int,
        arg2: float,
        arg3_with_very_long_name: list,
) -> None:
    print('Hello world')


result = func2(
    12345,
    3.1415926,
    [1, 2, 3],
)

result = [
    123,
    456,
    789,
    -123,
    -456,
]

something = {
    'a': 1,
    'b': 2,
    'c': 3,
}

some_tuple = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
)


class A:
    def __init__(
            self, a, b, c, d
    ):
        print('hello world')


class B:
    def __init__(
            self,
            a,
            b,
            c,
            d,
    ):
        print('hello world')


# Line length limit: 30 chars,
# which is right here:       |

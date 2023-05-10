# --function-definition-extra-indent = True
# --other-line-continuation-extra-indent = True
def function(
                arg1_with_very_long_name: int,
                arg2_with_very_long_name: float,
                arg3_with_very_long_name: list,
):
        print('Hello world')


def func2(
                arg1_with_very_long_name: int,
                arg2_with_very_long_name: float,
                arg3_with_very_long_name: list,
) -> None:
        print('Hello world')


def func3(a, b, c, d, e) -> int:
        return 2


def outer(
                arg1_with_very_long_name: int,
                *,
                arg2_with_very_long_name: float,
                arg3_with_very_long_name: list,
) -> int:
        def middle(
                        arg1_with_very_long_name: int,
                        arg2_with_very_long_name: float,
                        arg3_with_very_long_name: list,
                        *args,
        ):
                def inner(
                                arg1_with_very_long_name: int,
                                arg2_with_very_long_name: float,
                                arg3_with_very_long_name: list,
                                *args,
                                **kwargs,
                ):
                        return 1

                print('middle layer')
                return 2

        return 3


class A:
        def __init__(
                        self,
                        arg1_with_very_long_name: int,
                        arg2_with_very_long_name: float,
                        *,
                        arg3_with_very_long_name: list,
        ) -> None:
                print('hello world')

        def outer(
                        self,
                        arg1_with_very_long_name: int,
                        *,
                        arg2_with_very_long_name: float,
                        arg3_with_very_long_name: list,
        ) -> int:
                def middle(
                                arg1_with_very_long_name: int,
                                arg2_with_very_long_name: float,
                                arg3_with_very_long_name: list,
                                *args,
                ):
                        def inner(
                                        arg1_with_very_long_name: int,
                                        arg2_with_very_long_name: float,
                                        arg3_with_very_long_name: list,
                                        *args,
                                        **kwargs,
                        ):
                                class B:
                                        def __init__(
                                                        self,
                                                        arg1_with_very_long_name: int,
                                                        arg2_with_very_long_name: float,
                                                        arg3_with_very_long_name: list,
                                                        *args,
                                                        **kwargs,
                                        ):
                                                print('initialized')

                                return 1

                        print('middle layer')
                        return 2

                return 3


aa = [
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
]


bb = func1(
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
)


cc = {
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                value_with_very_very_very_very_very_very_long_name,
                123123123123123123123123123123123123123123123123123,
                'value_with_very_very_very_very_very_very_long_name',
}


if (
                value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
                and value_with_very_very_very_very_very_very_long_name
):
        print(123)


some_val_with_very_long_name = (
                'very very very long string' + 'this is an even longer string'
)

from dataclasses import dataclass

variable_1 = "very very very very very very very very very very very very very very long string"

variable_2 = "very very very very very very very very very very very very very very very long string"

variable_3 = 'very very very very very very very very very very very very very very long string'


@dataclass
class E:
    f: str = ""


@dataclass
class D:
    e: E = None


@dataclass
class C:
    d: D = None


@dataclass
class B:
    c: C = None


@dataclass
class A:
    b: B = None



a = A(B(C(D(E("")))))

a.b.c.d.e.some_attr = ("Once upon a time there is"  " a village alongside the river that flows quitely.")

a.b.c.d.e = "Once upon a time there is"  " a village alongside the river that flows quitely."

a.b.c.d.e = "Once upon a time there is"		" a village alongside the river that flows quitely."  # two tabs

a.b.c.d.e = ("Once upon a time there is"  " a village alongside the river that flows quitely.")

a.b.c = "Once upon a time there is"   " a village alongside the river that flows quitely. QED"

a.b.c = "Once upon a time there is"   " a village alongside the river that flows quitely. The end."

abc = "this line has two parts; the first string is already long than the line limit of 88 characters;" " this is the 2nd part"

"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."


result_1 = (  # aaa
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

result_2 = (
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb
)

result_3 = (
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)  # ccc

result_4 = (  # aaa
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb
)

result_5 = (
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb
)  # ccc

result_6 = (  # aaa
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)  # ccc

result_7 = (  # aaa
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb
)  # ccc


(
    "my very long string that shouldn't get formatted even if it goes over the 88 char"
    " limit like it does now"
)

three_strings_1 = (
    "What if we have inline comments on "  # aaa
    "each line of a bad split? In that "  # bbb
    "case, should we just leave it alone?"  # ccc
)

three_strings_2 = (
    "a"  # aa
    "b"  # bb
    "c"  # cc
)


# output
from dataclasses import dataclass

variable_1 = "very very very very very very very very very very very very very very long string"

variable_2 = "very very very very very very very very very very very very very very very long string"

variable_3 = "very very very very very very very very very very very very very very long string"


@dataclass
class E:
    f: str = ""


@dataclass
class D:
    e: E = None


@dataclass
class C:
    d: D = None


@dataclass
class B:
    c: C = None


@dataclass
class A:
    b: B = None


a = A(B(C(D(E("")))))

a.b.c.d.e.some_attr = "Once upon a time there is" " a village alongside the river that flows quitely."

a.b.c.d.e = "Once upon a time there is" " a village alongside the river that flows quitely."

a.b.c.d.e = (
    "Once upon a time there is" " a village alongside the river that flows quitely."
)  # two tabs

a.b.c.d.e = "Once upon a time there is" " a village alongside the river that flows quitely."

a.b.c = "Once upon a time there is" " a village alongside the river that flows quitely. QED"

a.b.c = "Once upon a time there is" " a village alongside the river that flows quitely. The end."

abc = "this line has two parts; the first string is already long than the line limit of 88 characters;" " this is the 2nd part"

"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."


result_1 = (  # aaa
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

result_2 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb

result_3 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # ccc

result_4 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # aaa  # bbb

result_5 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # bbb  # ccc

result_6 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # aaa  # ccc

result_7 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # aaa  # bbb  # ccc


("my very long string that shouldn't get formatted even if it goes over the 88 char" " limit like it does now")

three_strings_1 = (
    "What if we have inline comments on "  # aaa
    "each line of a bad split? In that "  # bbb
    "case, should we just leave it alone?"  # ccc
)

three_strings_2 = "a" "b" "c"  # aa  # bb  # cc

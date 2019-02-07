from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List
import string
import functools


def int_to_string(x: int) -> str:
    # unicode point of the character 0
    offset = ord("0")
    is_neg = False
    if x < 0:
        x *= -1
        is_neg = True
    s: List[int] = []
    while True:
        s.append(chr(offset + x % 10))
        x //= 10
        if x == 0:
            break
    return ("-" if is_neg else "") + "".join(reversed(s))


def string_to_int(s: str) -> int:
    offset = ord("0")
    neg = 1
    if s[0] == "-":
        s = s[1:]
        neg = -1
    n = 0
    p = 1
    for c in reversed(s):
        n += (ord(c) - offset) * p
        p *= 10
    return n * neg


# Solutions from book
def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord("0") + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ("-" if is_negative else "") + "".join(reversed(s))


def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == "-" :],
        0,
    ) * (-1 if s[0] == "-" else 1)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )

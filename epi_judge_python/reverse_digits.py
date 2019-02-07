from test_framework import generic_test


# convert it to a string trick
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    r = int(str(sign * x)[::-1])
    return sign * r


# divide by tens and take modulo
# O(n) where n is the number of digits
def reverse(x: int) -> int:
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))

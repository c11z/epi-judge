from test_framework import generic_test


# brute force
# make sure to iterate on abs(y) -1 times
# invert result if y is negative
def power(x: float, y: int) -> float:
    if y == 0:
        return 1
    result = x
    power = y
    if y < 0:
        power = -y
    for n in range(power - 1):
        result *= x
    if y < 0:
        result = 1.0 / result
    return result


# recursive
# number of mulitplications is at most twice the index of y's most significant bit
# implies O(n) time complexity
# I don't understand this yet
def power(x: float, y: int) -> float:
    result: float = 1.0
    power = y
    if y < 1:
        power = -power
        x = 1.0 / x
    while power:
        if power & 1:
            result *= x
        x *= x
        power >>= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))

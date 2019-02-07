from test_framework import generic_test


# right shift through all the bits
# result flips if the last bit is 1
# result is 0 if number of 1s is odd and is 1 if it is even
# time complexity is O(n) where n is the number of bits in x
def parity(x: int) -> int:
    result: int = 0
    while x:
        result ^= (x & 1)
        x >>= 1
    return result


# this flips result on every loop,
# but each iteration we drop the lowest set bit
# so we only loop on each bit that is 1
def parity2(x: int) -> int:
    result: int = 0
    while x:
        result ^= 1
        x &= x - 1 # drops the lowest set bit of x
    return result


# the parity of the number is the same
# as the parity of the left side of bits
# xor'd with the right side of bits
# this can be chased down to a single bit
# which can be masked and isolated as the parity
def parity3(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

# right propogate the right most set bit
def right_prop(x: int) -> int:
    return x | (x - 1)


# return the modulo of x mod y
# if y is a power of two
# works because binary numbers
# that are a power of 2 have a single left most bit
# xor erases that bit which leaves the modulo
def mod_pow_two(x: int, y: int) -> int:
    return x ^ y


# binary powers of two have single left most bit set
# this works because x - 1
# would then be a left most 0 and the rest would be 1s
# and them together and you will have 0
# so return the negative
def is_pow_two(x: int) -> int:
    return not (x & (x - 1))


if __name__ == '__main__':
    assert right_prop(int('01010000', 2)) == int('01011111', 2)
    assert right_prop(int('01010100', 2)) == int('01010111', 2)
    assert right_prop(int('10000000', 2)) == int('11111111', 2)
    assert right_prop(int('01010001', 2)) == int('01010001', 2)

    assert mod_pow_two(77, 64) == 13
    assert mod_pow_two(64, 64) == 0
    assert mod_pow_two(65, 64) == 1
    assert mod_pow_two(84, 64) == 20

    assert is_pow_two(2) == True
    assert is_pow_two(64) == True
    assert is_pow_two(7) == False
    assert is_pow_two(10) == False

    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity3))

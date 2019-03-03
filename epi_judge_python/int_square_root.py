from test_framework import generic_test

# brute force solution
# square every number from 0 to k and find when it goes over
# O(k) time complexity
# O(1) space complexity
def square_root(k: int) -> int:
    # k + 2 to satisfy lower bound edge cases when k = 0, 1, or 2
    for i in range(k + 2):
        if i * i > k:
            return i - 1


# uses binary search to find exactly where ^2 is over k
# O(logn) time complexity
# O(1) space complexity
def square_root(k: int) -> int:
    left: int = 0
    right: int = k
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )

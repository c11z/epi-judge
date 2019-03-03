from test_framework import generic_test
from typing import List

# use binary search to look for transition of cycle
# O(logn) time complexity
# O(1) space complexity
# note that if elements are repeated then this method does not work
def search_smallest(A: List[int]):
    left: int = 0
    right: int = len(A) - 1
    while left < right:
        mid: int = left + (right - left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:  # A[mid] < A[right]
            right = mid
    return left


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )

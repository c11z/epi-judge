import bisect
from test_framework import generic_test
from typing import List, Optional


# takes in two steps
# first find a k and then walk left until it is not k anymore
# O(logn) time complexity, same as as binary search, worst case is O(n)
# O(1) space complexity
def search_first_of_k(A: List[int], k: int) -> int:
    def binary_search() -> Optional[int]:
        # binary search on A
        l: int = 0
        h: int = len(A) - 1
        while l <= h:
            m = l + (h - l) // 2
            if k > A[m]:
                l = m + 1
            elif k == A[m]:
                return m
            else:
                h = m - 1
        return None

    r = binary_search()
    if r is None:
        return -1
    else:
        # walk to the left and check if there is a prior version of k
        while r > -1 and A[r] == k:
            r -= 1
        return r + 1


# solution from book
def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )

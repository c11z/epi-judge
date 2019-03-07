import random
import operator
from test_framework import generic_test
from typing import List, Callable

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
# Brute force, O(nlogn) time complexity for the sort and lookup
# O(1) extra space since sort is in place
def find_kth_largest1(k: int, A: List[int]):
    A.sort()
    return A[len(A) - k]


def find_kth_largest(k: int, A: List[int]):
    def find_kth(comp: Callable[[int, int], bool]):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left: int, right: int, pivot_idx: int):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

        raise IndexError("no k-th node in array A")

    return find_kth(operator.gt)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py", "kth_largest_in_array.tsv", find_kth_largest
        )
    )

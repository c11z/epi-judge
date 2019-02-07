import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# silly inefficient
# O(n^2) time and O(1) space
# it is pretty easy to avoid the inner loop
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in range(len(A) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    return None


# two pass, memoize smaller and larger index instead of inner loop
# O(n) time and O(1) space
# requires two passes
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for j in range(len(A) - 1, -1, -1):
        if A[j] > pivot:
            A[j], A[larger] = A[larger], A[j]
            larger -= 1
    return None


# one pass, track 4 different groups, with three different index trackers
# O(n) time and O(1)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot: int = A[pivot_index]
    smaller: int = 0
    equal: int = 0
    larger: int = len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif A[equal] > pivot:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        else:
            # equals to pivot
            equal += 1
    return None


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

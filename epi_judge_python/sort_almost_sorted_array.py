import itertools
from test_framework import generic_test
from typing import List, Iterator
from heapq import heappush, heappop, heappushpop


# keep k + 1 elements in the heap to insure min is lowest
# O(n log k) time complexity
# O(k) extra space
def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    min_heap: List[int] = []
    result: List[int] = []
    for _ in range(k + 1):
        new = next(sequence, None)
        if new is not None:
            heappush(min_heap, new)
    while min_heap:
        result.append(heappop(min_heap))
        new = next(sequence, None)
        if new is not None:
            heappush(min_heap, new)
    return result


# solution from the book
# uses heappushpop which is faster than heappush and heappop consecutively
def sort_approximately_sorted_array(sequence, k):

    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heappush(min_heap, x)

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )

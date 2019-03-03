from test_framework import generic_test
from typing import List, Optional
from heapq import heappush, heappop, merge


# trick is to convert list of lists into list of iterators
# one loop to put the first element in to the heap
# always get next number from the array that had the smallest
# O(n log k) time complexity where k is the number of lists
# O(k) extra space complexity to store the heap
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result: List[int] = []
    min_heap: List[int] = []
    sorted_array_iters = [iter(a) for a in sorted_arrays]

    # set up min_heap with first elements from each array
    for i, itr in enumerate(sorted_array_iters):
        first: Optional[int] = next(itr, None)
        if first is not None:
            heappush(min_heap, (first, i))

    while min_heap:
        smallest, array_idx = heappop(min_heap)
        result.append(smallest)
        new: Optional[int] = next(sorted_array_iters[array_idx], None)
        if new is not None:
            heappush(min_heap, (new, array_idx))

    return result


# from book pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )

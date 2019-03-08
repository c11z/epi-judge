from test_framework import generic_test
from typing import List


# find the intersect of two sorted arrays
# duplicates allowed in individual arrays
# this is an inefficient way, use set math find intersection
# the problem is that you have to re-sort the result
# O(nlogn) time complexity
# O(n) extra space
# n is the total unique values in both lists
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    return sorted(list(set(A) & set(B)))


# O(n) solution should be possible
# sliding window to avoid n^2
# knowing smaller list will allow to escape early
# memo seen values to avoid adding duplicates to result
# worst case is that there is a value in A not in B so we must look at all values
# A = [ 1, 2, 3]
# B = [ 2. 3. 4, 5]
# res = [2, 3]
# O(n) time complexity, where n is the combined length of the lists
# O(p) space complexity where p is the unique intersection of A and B
# in real time this is actually slower than the above solution
# maybe because the sorted and set init functions are highly optimized
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # ensure A is smaller than B
    if len(A) > len(B):
        A, B = B, A
    res: List[int] = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if not res or A[i] != res[-1]:
            while B[j] < A[i] and j < len(B) - 1:
                j += 1
            if A[i] == B[j]:
                res.append(A[i])
        i += 1
    return res


# solution from book
# fastest of all, although the "a in B" is confusing to me
# and I would assume is less efficient than the above solution
# but is faster because it is optimized
def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )

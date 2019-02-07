from test_framework import generic_test
from typing import List
import math
import collections
# check if a partially filled matrix has any conflicts
# conflicts are tracked with boolean arrays as cheap
# hashmap to see if any of the values in the zones are repeated
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # check columns
    for col in partial_assignment:
        check: List[bool] = [False]*10
        for v in col:
            if v != 0 and check[v]:
                return False
            else:
                check[v] = True

    # check rows
    for i in range(9):
        check: List[bool] = [False]*10
        for col in partial_assignment:
            v = col[i]
            if v != 0 and check[v]:
                return False
            else:
                check[v] = True

    # check subarrays
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            check: List[bool] = [False]*10
            for dx in range(3):
                for dy in range(3):
                    v = partial_assignment[x + dx][y + dy]
                    if v != 0 and check[v]:
                        return False
                    else:
                        check[v] = True
    return True


# Solutions from book
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):

    # Return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col] contains any
    # duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return
    # False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (
            I + 1)) for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
        collections.Counter(k for i, row in enumerate(partial_assignment)
                            for j, c in enumerate(row) if c != 0
                            for k in ((i, str(c)), (str(c), j),
                                      (i / region_size, j / region_size,
                                       str(c)))).values(),
        default=0) <= 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))

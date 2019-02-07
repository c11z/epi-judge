from test_framework import generic_test
from typing import List
from math import ceil


# create a layer function that walks all four sides
# have an edge case for the odd matrix in the middle
# O(n^2) time complexity O(1) space
def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    spiral: List[int] = []
    for offset in range(ceil(0.5 * len(square_matrix))):
        spiral += layer(offset, square_matrix)
    return spiral

def layer(offset: int, square_matrix: List[List[int]]) -> List[int]:
    spiral: List[int] = []
    boundary = len(square_matrix) - offset - 1
    # if at center of odd matrix return center
    if offset == boundary:
        return [square_matrix[offset][offset]]
    # walk right
    for c in range(offset, boundary):
        spiral.append(square_matrix[offset][c])
    # walk down
    for r in range(offset, boundary):
        spiral.append(square_matrix[r][boundary])
    # walk left
    for c in range(boundary, offset, -1):
        spiral.append(square_matrix[boundary][c])
    # walk up
    for r in range(boundary, offset, -1):
        spiral.append(square_matrix[r][offset])
    return spiral


# solution from book, one pass
# clever is that it backfills the matrix with 0s
# and uses that to detect direction changes
# doesn't have to be 0s, could be any value
# guaranteed to not be in the matrix
# O(n^2) time complexity O(1) space
def matrix_in_spiral_order(square_matrix):

    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))

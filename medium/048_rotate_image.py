"""
Problem 48: Rotate Image
https://leetcode.com/problems/rotate-image/

Rotate an n x n matrix 90 degrees clockwise in place.

Examples:
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output:        [[7,4,1],[8,5,2],[9,6,3]]
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate in place by transposing, then reversing every row.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in matrix:
            row.reverse()


def rotate_and_return(matrix: List[List[int]]) -> List[List[int]]:
    Solution().rotate(matrix)
    return matrix


if __name__ == "__main__":
    test(
        rotate_and_return,
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        "Test 1 - Three by three matrix",
    )
    test(
        rotate_and_return,
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        "Test 2 - Four by four matrix",
    )
    test(rotate_and_return, [[1]], [[1]], "Test 3 - Single cell")

"""
Reflection:
The key is to treat rotation as two simple transformations: transpose the
matrix across its main diagonal, then reverse each row. This avoids allocating
another n x n matrix while still touching every value only a constant number
of times. The transpose only swaps values above the diagonal, so no pair is
swapped twice.
"""

"""
Problem 73: Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n matrix, if an element is 0, set its entire row and column to 0.
The update must happen in place.

Examples:
Input:  matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output:        [[1,0,1],[0,0,0],[1,0,1]]
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Use the first row and column as in-place markers.

        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][col] == 0 for col in range(cols))
        first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0


def set_zeroes_and_return(matrix: List[List[int]]) -> List[List[int]]:
    Solution().setZeroes(matrix)
    return matrix


if __name__ == "__main__":
    test(
        set_zeroes_and_return,
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        "Test 1 - Interior zero",
    )
    test(
        set_zeroes_and_return,
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        "Test 2 - First row markers",
    )
    test(set_zeroes_and_return, [[1]], [[1]], "Test 3 - No zeroes")

"""
Reflection:
The direct approach stores every affected row and column in sets, which costs
O(m + n) extra space. The first row and first column can store those same
markers instead. Because they also need to preserve their own zero status, we
record that status before using them as markers and update them last.
"""

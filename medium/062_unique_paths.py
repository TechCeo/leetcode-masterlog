"""
Problem 62: Unique Paths
https://leetcode.com/problems/unique-paths/

Given an m x n grid, return the number of unique paths from the top-left corner
to the bottom-right corner. You may only move down or right.

Example:
Input: m = 3, n = 7
Output: 28
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Build path counts row by row using a one-dimensional DP array.

        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """
        paths = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                paths[col] += paths[col - 1]

        return paths[-1]


if __name__ == "__main__":
    sol = Solution()

    test(sol.uniquePaths, 3, 7, 28, "Test 1 - Three by seven grid")
    test(sol.uniquePaths, 3, 2, 3, "Test 2 - Three by two grid")
    test(sol.uniquePaths, 1, 1, 1, "Test 3 - Single cell")
    test(sol.uniquePaths, 1, 5, 1, "Test 4 - Single row")
    test(sol.uniquePaths, 4, 4, 20, "Test 5 - Square grid")

"""
Reflection:
Each cell's path count is the sum of the cell above it and the cell to its left.
A full 2D table works, but each row only depends on the current row's left value
and the previous row's value in the same column. A one-dimensional array keeps
that information compactly: paths[col] starts as the value from above, then we
add paths[col - 1] from the left.
"""

"""
Problem 463: Island Perimeter
https://leetcode.com/problems/island-perimeter/

You are given row x col grid representing a map where grid[i][j] = 1 represents
land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally or vertically. The grid is completely
surrounded by water, and there is exactly one island.

Return the perimeter of the island.

Example:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Count exposed sides for every land cell.

        Time Complexity: O(m * n) - Every cell is checked once.
        Space Complexity: O(1) - No extra data structure grows with input size.
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

        return perimeter


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.islandPerimeter,
        [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
        16,
        "Test 1 - Example island",
    )
    test(sol.islandPerimeter, [[1]], 4, "Test 2 - Single land cell")
    test(sol.islandPerimeter, [[1, 0]], 4, "Test 3 - One land one water")
    test(sol.islandPerimeter, [[1, 1], [1, 1]], 8, "Test 4 - Solid square")


"""
Reflection:
Each land cell starts with four exposed sides.

When two land cells touch, the shared edge should not count toward the
perimeter. Checking only the top and left neighbors avoids double counting:
- subtract 2 for a land neighbor above
- subtract 2 for a land neighbor to the left

This keeps the solution simple while still visiting each cell only once.
"""

"""
Problem 200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land)
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.

Examples:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS flood-fill approach.

        Strategy:
        - Scan every cell in the grid.
        - When land is found, count a new island.
        - Sink all connected land from that starting point using DFS.

        Time Complexity: O(m * n) - Each cell is visited at most once.
        Space Complexity: O(m * n) - Recursive call stack in the worst case.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.numIslands,
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"],
        ],
        1,
        "Test 1 - One island",
    )

    test(
        sol.numIslands,
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
        ],
        3,
        "Test 2 - Three islands",
    )

    test(sol.numIslands, [["0","0"], ["0","0"]], 0, "Test 3 - All water")
    test(sol.numIslands, [["1"]], 1, "Test 4 - Single land cell")

"""
Problem 994: Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:
- 0 represents an empty cell.
- 1 represents a fresh orange.
- 2 represents a rotten orange.

Every minute, any fresh orange that is horizontally or vertically adjacent
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no fresh orange
remains. If this is impossible, return -1.

Examples:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Input: grid = [[0,2]]
Output: 0

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2
"""

from collections import deque
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS approach.

        Strategy:
        - Add every initially rotten orange to the queue.
        - Count the number of fresh oranges.
        - Process the queue one minute at a time, rotting adjacent oranges.
        - If fresh oranges remain after BFS, they were unreachable.

        Time Complexity: O(m * n) - Each cell is processed at most once.
        Space Complexity: O(m * n) - The queue may contain every orange.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    next_row = row + dr
                    next_col = col + dc

                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.orangesRotting,
        [[2,1,1], [1,1,0], [0,1,1]],
        4,
        "Test 1 - All oranges rot",
    )
    test(
        sol.orangesRotting,
        [[2,1,1], [0,1,1], [1,0,1]],
        -1,
        "Test 2 - Unreachable orange",
    )
    test(sol.orangesRotting, [[0,2]], 0, "Test 3 - No fresh oranges")
    test(sol.orangesRotting, [[1]], -1, "Test 4 - No rotten oranges")
    test(sol.orangesRotting, [[2,1,1,1]], 3, "Test 5 - Single row")

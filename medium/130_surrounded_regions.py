"""
Problem 130: Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given an m x n board containing 'X' and 'O', capture all regions that are
4-directionally surrounded by 'X'.

A region is captured by flipping all surrounded 'O' cells into 'X'. Any 'O'
connected to the border cannot be captured.

Examples:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Mark border-connected regions, then flip the rest.

        Strategy:
        - Any 'O' connected to a border 'O' is safe.
        - Temporarily mark safe cells as 'S'.
        - Flip remaining 'O' cells to 'X'.
        - Restore safe cells back to 'O'.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) - Recursive stack in the worst case.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def mark_safe(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != "O"
            ):
                return

            board[r][c] = "S"
            mark_safe(r + 1, c)
            mark_safe(r - 1, c)
            mark_safe(r, c + 1)
            mark_safe(r, c - 1)

        for r in range(rows):
            mark_safe(r, 0)
            mark_safe(r, cols - 1)

        for c in range(cols):
            mark_safe(0, c)
            mark_safe(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


def solve_and_return(board):
    Solution().solve(board)
    return board


if __name__ == "__main__":
    test(
        solve_and_return,
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"],
        ],
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"],
        ],
        "Test 1 - Capture surrounded region",
    )
    test(
        solve_and_return,
        [["X"]],
        [["X"]],
        "Test 2 - Single cell",
    )
    test(
        solve_and_return,
        [["O","O"], ["O","O"]],
        [["O","O"], ["O","O"]],
        "Test 3 - All border-connected",
    )

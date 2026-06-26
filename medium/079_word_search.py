"""
Problem 79: Word Search
https://leetcode.com/problems/word-search/

Return True if a word can be built from sequentially adjacent board cells.
Cells may be adjacent horizontally or vertically, and each cell may be used
at most once in a path.

Examples:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Try each matching cell as a starting point and backtrack through paths.

        Time Complexity: O(m * n * 4^L), where L is the word length.
        Space Complexity: O(L) for the recursive call stack.
        """
        rows, cols = len(board), len(board[0])

        def search(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True

            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != word[index]
            ):
                return False

            letter = board[row][col]
            board[row][col] = "#"
            found = (
                search(row + 1, col, index + 1)
                or search(row - 1, col, index + 1)
                or search(row, col + 1, index + 1)
                or search(row, col - 1, index + 1)
            )
            board[row][col] = letter

            return found

        for row in range(rows):
            for col in range(cols):
                if search(row, col, 0):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    test(Solution().exist, board, "ABCCED", True, "Test 1 - Word exists")
    test(Solution().exist, board, "SEE", True, "Test 2 - Different valid path")
    test(Solution().exist, board, "ABCB", False, "Test 3 - Cannot reuse a cell")
    test(Solution().exist, [["A"]], "A", True, "Test 4 - Single cell match")
    test(Solution().exist, [["A"]], "B", False, "Test 5 - Single cell mismatch")

"""
Reflection:
This is a path-search problem, so DFS with backtracking fits naturally. Marking
the current board cell in place prevents revisiting it in the same path without
needing a separate visited set. Restoring the letter afterward is essential:
each starting cell and branch needs a clean board to explore independently.
"""

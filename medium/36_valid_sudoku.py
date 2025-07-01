"""
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A valid Sudoku board (partially filled) is not necessarily solvable.
- The board is always 9x9 and contains digits or '.'.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: True

Example 2 (Invalid):
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","8",".","3",".",".","5"],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: False
"""

from typing import List
from collections import defaultdict
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def isValidSudoku_explicit(self, board: List[List[str]]) -> bool:
        # Validate rows
        for row in range(9):
            row_set = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in row_set:
                    return False
                row_set.add(board[row][i])

        # Validate columns
        for col in range(9):
            col_set = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in col_set:
                    return False
                col_set.add(board[i][col])

        # Validate 3x3 sub-boxes
        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in square_set:
                        return False
                    square_set.add(board[row][col])

        return True

    def isValidSudoku_optimized(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if (val in rowSet[i] or
                    val in colSet[j] or
                    val in squareSet[(i // 3, j // 3)]):
                    return False
                rowSet[i].add(val)
                colSet[j].add(val)
                squareSet[(i // 3, j // 3)].add(val)

        return True


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    valid_board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    invalid_board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","8",".","3",".",".","5"],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    test(sol.isValidSudoku_explicit, valid_board, True, "Explicit - Valid")
    test(sol.isValidSudoku_explicit, invalid_board, False, "Explicit - Invalid")

    test(sol.isValidSudoku_optimized, valid_board, True, "Optimized - Valid")
    test(sol.isValidSudoku_optimized, invalid_board, False, "Optimized - Invalid")

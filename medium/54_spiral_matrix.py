"""
54. Spiral Matrix

Given an m x n matrix, return all elements in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Boundary Traversal

        Maintain four boundaries:
        - top row
        - bottom row
        - left column
        - right column

        Shrink boundaries as we traverse.

        Time Complexity: O(m * n)
        Space Complexity: O(1) (excluding output)
        """

        numRows = len(matrix)
        numCols = len(matrix[0]) if numRows > 0 else 0

        topRow = 0
        btmRow = numRows - 1
        leftCol = 0
        rightCol = numCols - 1

        result = []

        while topRow <= btmRow and leftCol <= rightCol:

            # Traverse top row
            for i in range(leftCol, rightCol + 1):
                result.append(matrix[topRow][i])
            topRow += 1

            # Traverse right column
            for i in range(topRow, btmRow + 1):
                result.append(matrix[i][rightCol])
            rightCol -= 1

            # Traverse bottom row
            if topRow <= btmRow:
                for i in range(rightCol, leftCol - 1, -1):
                    result.append(matrix[btmRow][i])
                btmRow -= 1

            # Traverse left column
            if leftCol <= rightCol:
                for i in range(btmRow, topRow - 1, -1):
                    result.append(matrix[i][leftCol])
                leftCol += 1

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.spiralOrder,
         [[1,2],[3,4]],
         [1,2,4,3],
         "2x2 Matrix")

    test(sol.spiralOrder,
         [[1,2,3],[4,5,6],[7,8,9]],
         [1,2,3,6,9,8,7,4,5],
         "3x3 Matrix")

    test(sol.spiralOrder,
         [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
         [1,2,3,4,8,12,11,10,9,5,6,7],
         "Rectangular Matrix")

    test(sol.spiralOrder,
         [[1]],
         [1],
         "Single Element")

    test(sol.spiralOrder,
         [[1,2,3,4]],
         [1,2,3,4],
         "Single Row")

    test(sol.spiralOrder,
         [[1],[2],[3],[4]],
         [1,2,3,4],
         "Single Column")


"""
Reflection:
This problem is less about algorithms and more about careful boundary management.

The key idea is maintaining four shrinking boundaries:
top, bottom, left, right.

The tricky part is avoiding duplicate traversals when the matrix collapses inward,
which is why the boundary checks (if top <= bottom, etc.) are critical.

This is a great example of a problem where correctness depends on handling edge cases cleanly.
"""
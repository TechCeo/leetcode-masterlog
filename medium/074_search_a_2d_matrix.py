"""
Problem 74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix and a target value.
Each row is sorted in non-decreasing order, and the first integer of each row
is greater than the last integer of the previous row.

Return True if target exists in the matrix, else False.

Examples:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10 → Output: True
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15 → Output: False

Constraints:
- 1 <= m, n <= 100
- -10000 <= matrix[i][j], target <= 10000
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test
from typing import List


# Brute-force linear scan
class BruteForce:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(m * n) – Scan all elements
        Space: O(1)
        """
        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False


# Optimal binary search approach
class BinarySearchFlattened:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(log(m * n)) – Treat 2D matrix as a 1D sorted array
        Space: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    print("\nBrute Force Solution:")
    bf = BruteForce()
    test(bf.searchMatrix, [[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10, True, "Test 1")
    test(bf.searchMatrix, [[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15, False, "Test 2")

    print("\n--------------------------------------------------")
    print("Binary Search Solution:")
    bs = BinarySearchFlattened()
    test(bs.searchMatrix, [[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10, True, "Test 1")
    test(bs.searchMatrix, [[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15, False, "Test 2")

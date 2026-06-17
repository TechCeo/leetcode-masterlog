"""
Problem 733: Flood Fill
https://leetcode.com/problems/flood-fill/

You are given an image represented by an m x n integer grid, where image[i][j]
represents the pixel value of the image.

Starting from image[sr][sc], replace the color of that pixel and every
4-directionally connected pixel with the same original color with newColor.

Examples:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        newColor: int,
    ) -> List[List[int]]:
        """
        DFS flood-fill approach.

        Time Complexity: O(m * n) - In the worst case, every pixel is visited.
        Space Complexity: O(m * n) - Recursive stack in the worst case.
        """
        original_color = image[sr][sc]
        if original_color == newColor:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or image[r][c] != original_color
            ):
                return

            image[r][c] = newColor
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.floodFill,
        [[1,1,1], [1,1,0], [1,0,1]],
        1,
        1,
        2,
        [[2,2,2], [2,2,0], [2,0,1]],
        "Test 1 - Fill connected region",
    )
    test(
        sol.floodFill,
        [[0,0,0], [0,0,0]],
        0,
        0,
        0,
        [[0,0,0], [0,0,0]],
        "Test 2 - Same color no-op",
    )
    test(sol.floodFill, [[1]], 0, 0, 3, [[3]], "Test 3 - Single pixel")

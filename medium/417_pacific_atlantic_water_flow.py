"""
Problem 417: Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of heights, return all coordinates where water can flow
to both the Pacific and Atlantic oceans.

Water can flow from a cell to another cell 4-directionally if the next cell's
height is less than or equal to the current cell's height.

Examples:
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""

from typing import List, Set, Tuple
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Reverse DFS from ocean borders.

        Instead of asking where each cell can flow, start from each ocean and
        move inward only to cells with height greater than or equal to the
        current cell. Cells reached by both searches can flow to both oceans.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r: int, c: int, visited: Set[Tuple[int, int]], prev_height: int) -> None:
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return [[r, c] for r, c in pacific & atlantic]


def sorted_pacific_atlantic(heights):
    return sorted(Solution().pacificAtlantic(heights))


if __name__ == "__main__":
    test(
        sorted_pacific_atlantic,
        [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4],
        ],
        sorted([[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]),
        "Test 1 - Multiple shared cells",
    )
    test(sorted_pacific_atlantic, [[1]], [[0, 0]], "Test 2 - Single cell")
    test(
        sorted_pacific_atlantic,
        [[1, 2], [4, 3]],
        sorted([[0, 1], [1, 0], [1, 1]]),
        "Test 3 - Small slope",
    )

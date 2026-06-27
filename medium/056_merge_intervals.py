"""
Problem 56: Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals and return the non-overlapping intervals.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort by start time, then grow the most recent merged interval whenever
        the next interval overlaps it.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return []

        sorted_intervals = sorted(intervals)
        merged = [sorted_intervals[0]]

        for start, end in sorted_intervals[1:]:
            last_interval = merged[-1]

            if start <= last_interval[1]:
                last_interval[1] = max(last_interval[1], end)
            else:
                merged.append([start, end])

        return merged


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.merge,
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 6], [8, 10], [15, 18]],
        "Test 1 - Basic overlap",
    )
    test(sol.merge, [[1, 4], [4, 5]], [[1, 5]], "Test 2 - Touching intervals")
    test(
        sol.merge,
        [[1, 4], [0, 4]],
        [[0, 4]],
        "Test 3 - Unsorted contained interval",
    )
    test(sol.merge, [], [], "Test 4 - Empty input")

"""
Reflection:
Sorting is the move that turns a global overlap problem into a local one. Once
intervals are ordered by start time, every interval either merges with the last
answer interval or starts a brand-new range. This keeps the scan simple and
linear after the initial sort.
"""

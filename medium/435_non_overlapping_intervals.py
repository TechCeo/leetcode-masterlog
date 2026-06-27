"""
Problem 435: Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals, return the minimum number of intervals to remove
to make the rest non-overlapping.

Example:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Keep the interval that ends earliest whenever overlaps compete.

        Time Complexity: O(n log n)
        Space Complexity: O(n) for the sorted copy
        """
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
        removals = 0
        previous_end = sorted_intervals[0][1]

        for start, end in sorted_intervals[1:]:
            if start < previous_end:
                removals += 1
            else:
                previous_end = end

        return removals


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.eraseOverlapIntervals,
        [[1, 2], [2, 3], [3, 4], [1, 3]],
        1,
        "Test 1 - Remove one interval",
    )
    test(
        sol.eraseOverlapIntervals,
        [[1, 2], [1, 2], [1, 2]],
        2,
        "Test 2 - Duplicate overlapping intervals",
    )
    test(
        sol.eraseOverlapIntervals,
        [[1, 2], [2, 3]],
        0,
        "Test 3 - Already non-overlapping",
    )
    test(sol.eraseOverlapIntervals, [], 0, "Test 4 - Empty input")

"""
Reflection:
This is a greedy scheduling problem in disguise. To remove as few intervals as
possible, we want to keep as many non-overlapping intervals as possible. Sorting
by end time helps because the interval that finishes earliest leaves the most
space for future intervals. When another interval starts before the current end,
we remove it and keep the earlier-ending choice.
"""

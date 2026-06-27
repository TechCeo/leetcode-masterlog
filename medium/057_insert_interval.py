"""
Problem 57: Insert Interval
https://leetcode.com/problems/insert-interval/

Given a sorted list of non-overlapping intervals, insert a new interval and
merge if necessary.

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Add intervals before the new one, merge all overlaps into the new one,
        then append the remaining intervals.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        index = 0
        n = len(intervals)

        while index < n and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        while index < n and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        result.append(newInterval)

        while index < n:
            result.append(intervals[index])
            index += 1

        return result


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.insert,
        [[1, 3], [6, 9]],
        [2, 5],
        [[1, 5], [6, 9]],
        "Test 1 - Merge one interval",
    )
    test(
        sol.insert,
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
        [[1, 2], [3, 10], [12, 16]],
        "Test 2 - Merge multiple intervals",
    )
    test(sol.insert, [], [5, 7], [[5, 7]], "Test 3 - Empty interval list")
    test(
        sol.insert,
        [[1, 5]],
        [6, 8],
        [[1, 5], [6, 8]],
        "Test 4 - Insert after all intervals",
    )

"""
Reflection:
Because the input intervals are already sorted and non-overlapping, we do not
need to sort again. The solution has three clean phases: copy everything that
ends before the new interval, absorb every interval that overlaps it, and then
copy the rest. This is the interval equivalent of carefully splicing into an
ordered list.
"""

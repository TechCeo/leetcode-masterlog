"""
Problem 252: Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
determine if a person could attend all meetings.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: False
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Sort meetings by start time and check neighboring meetings for overlap.

        Time Complexity: O(n log n)
        Space Complexity: O(n) for the sorted copy
        """
        sorted_intervals = sorted(intervals)

        for index in range(1, len(sorted_intervals)):
            previous_end = sorted_intervals[index - 1][1]
            current_start = sorted_intervals[index][0]

            if current_start < previous_end:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.canAttendMeetings,
        [[0, 30], [5, 10], [15, 20]],
        False,
        "Test 1 - Overlapping meetings",
    )
    test(
        sol.canAttendMeetings,
        [[7, 10], [2, 4]],
        True,
        "Test 2 - Non-overlapping meetings",
    )
    test(
        sol.canAttendMeetings,
        [[1, 5], [5, 8], [8, 12]],
        True,
        "Test 3 - Back-to-back meetings",
    )
    test(sol.canAttendMeetings, [], True, "Test 4 - No meetings")

"""
Reflection:
Intervals become much easier once they are sorted by start time. After sorting,
we only need to compare each meeting with the one immediately before it. If the
current start is before the previous end, those two meetings overlap and one
person cannot attend both. Back-to-back meetings are allowed because ending at
time x and starting at time x does not overlap.
"""

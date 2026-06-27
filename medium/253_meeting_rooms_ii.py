"""
Problem 253: Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals, return the minimum number of
conference rooms required.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""

import heapq
from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Sort meetings by start time and use a min-heap to track the earliest
        room end time.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals)
        room_end_times = []

        for start, end in sorted_intervals:
            if room_end_times and room_end_times[0] <= start:
                heapq.heappop(room_end_times)

            heapq.heappush(room_end_times, end)

        return len(room_end_times)


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.minMeetingRooms,
        [[0, 30], [5, 10], [15, 20]],
        2,
        "Test 1 - Two rooms needed",
    )
    test(sol.minMeetingRooms, [[7, 10], [2, 4]], 1, "Test 2 - One room enough")
    test(
        sol.minMeetingRooms,
        [[1, 5], [2, 6], [3, 7], [8, 9]],
        3,
        "Test 3 - Three overlapping meetings",
    )
    test(sol.minMeetingRooms, [], 0, "Test 4 - No meetings")

"""
Reflection:
The heap represents rooms currently in use, storing only their end times. When
the earliest-ending room is free before the next meeting starts, that room can
be reused. Otherwise, we need another room. The largest heap size reached during
the scan is the number of simultaneous meetings, which is exactly the minimum
number of rooms required.
"""

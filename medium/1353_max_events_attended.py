# 1353. Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List
import heapq
from utils.test_utils import test


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Greedy + Min Heap approach:
        Sort events by start day, and each day:
            - Add all events starting that day to the heap
            - Remove past events from the heap
            - Attend the event with the earliest end day
        """
        events.sort()
        total_days = max(end for _, end in events)
        min_heap = []
        day = i = res = 0

        for day in range(1, total_days + 1):
            while i < len(events) and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                res += 1

        return res

# Time Complexity: O(N log N)
#   - Sorting: O(N log N)
#   - Heap operations: O(N log N) in total
#Space Complexity: O(N) for heap

# Reflection:
# This is a classic greedy scheduling problem that’s disguised in the form of days and ranges.
# The idea of attending events by earliest end date is powerful when combined with a priority queue.
# Initially tried brute-force but this heap-greedy combination is clean and optimal.

# Test Cases
s = Solution()
test(s.maxEvents, [[1, 2], [2, 3], [3, 4]], 3, "Example 1")
test(s.maxEvents, [[1, 2], [2, 3], [3, 4], [1, 2]], 4, "Example 2")
test(s.maxEvents, [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]], 4, "Overlap-heavy")
test(s.maxEvents, [[1, 1], [1, 1], [1, 1], [1, 1]], 1, "Single day events")
test(s.maxEvents, [[1, 100000], [2, 2], [2, 3], [3, 4]], 4, "Long span vs short")


# 1751_max_value_of_attending_events.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List
from functools import lru_cache
from bisect import bisect_right
from utils.test_utils import test

class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         """
#         Dynamic programming with binary search.

#         Sort events by end time, then for each event we either:
#         - Skip it and take max value up to i-1 with k events.
#         - Attend it: find last non-overlapping event before it, add current value to best from that index.

#         Time Complexity: O(n * k * log n)
#         Space Complexity: O(n * k)
#         """
#         events.sort(key=lambda x: x[1])  # sort by end day
#         n = len(events)
#         starts = [e[0] for e in events]
        
#         # dp[i][j]: max value using first i events and attending j events
#         dp = [[0] * (k + 1) for _ in range(n + 1)]

#         for i in range(1, n + 1):
#             s, e, v = events[i - 1]
#             # Binary search for last event that ends before current start
#             l = bisect_right([events[x][1] for x in range(n)], s - 1, 0, i - 1)
#             for j in range(1, k + 1):
#                 dp[i][j] = max(dp[i - 1][j], dp[l][j - 1] + v)
#         return dp[n][k]

     def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        start_days = [e[0] for e in events]
        n = len(events)

        @lru_cache(None)
        def dp(i: int, k_remaining: int) -> int:
            if i == n or k_remaining == 0:
                return 0

            skip = dp(i + 1, k_remaining)
            next_index = bisect_right(start_days, events[i][1])
            take = events[i][2] + dp(next_index, k_remaining - 1)

            return max(skip, take)

        return dp(0, k)



# Simple test utility
def test(func, *args):
    *inputs, expected, name = args
    try:
        result = func(*inputs)
        if result == expected:
            print(f"{name} ✅ Passed")
        else:
            print(f"{name} ❌ Failed")
            print(f"   Input: {tuple(inputs)}")
            print(f"   Output: {result}")
            print(f"   Expected: {expected}")
    except Exception as e:
        print(f"{name} ❌ Error")
        print(f"   Exception: {e}")

if __name__ == "__main__":
    sol = Solution()
    test(sol.maxValue, [[1,2,4],[3,4,3],[2,3,1]], 2, 7, "Example 1")
    test(sol.maxValue, [[1,2,4],[3,4,3],[2,3,10]], 2, 10, "Example 2")
    test(sol.maxValue, [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9, "Example 3")
    test(sol.maxValue, [[1,1000000000,1],[2,3,1000000],[3,4,1000000],[4,5,1000000]], 2, 2000000, "Large Range Test")

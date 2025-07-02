"""
875. Koko Eating Bananas

You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

Each hour, you may choose a pile and eat k bananas from it. If the pile has less than k bananas,
you eat the whole pile and move to the next in the next hour. You cannot eat from more than one pile per hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Leetcode link: https://leetcode.com/problems/koko-eating-bananas/
"""

from typing import List
import math
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test(sol.minEatingSpeed, [1, 4, 3, 2], 9, 2, "Test 1")
    test(sol.minEatingSpeed, [25, 10, 23, 4], 4, 25, "Test 2")
    test(sol.minEatingSpeed, [30, 11, 23, 4, 20], 5, 30, "Test 3")
    test(sol.minEatingSpeed, [30, 11, 23, 4, 20], 6, 23, "Test 4")
    test(sol.minEatingSpeed, [3, 6, 7, 11], 8, 4, "Test 5")

"""
Time Complexity: O(N log M), where:
- N is the number of piles
- M is the maximum bananas in a single pile (upper bound for k)
Space Complexity: O(1)

Reflection:
This is a classic "binary search on answer" pattern. The naive approach would test all possible values of k,
but binary search reduces the solution space efficiently. The key realization is to think of this
as a decision problem — "Can Koko finish all bananas at speed k?" — and use that to guide the binary search.
"""
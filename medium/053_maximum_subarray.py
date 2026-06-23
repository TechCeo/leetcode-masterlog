"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray with the largest
sum and return that sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum.
"""

import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm: extend the current subarray or start a new one.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current_sum = nums[0]
        best_sum = nums[0]

        for number in nums[1:]:
            current_sum = max(number, current_sum + number)
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.maxSubArray,
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        6,
        "Test 1 - Mixed values",
    )
    test(sol.maxSubArray, [1], 1, "Test 2 - Single element")
    test(sol.maxSubArray, [-8, -3, -6, -2, -5, -4], -2, "Test 3 - All negative")
    test(sol.maxSubArray, [5, 4, -1, 7, 8], 23, "Test 4 - Mostly positive")


"""
Reflection:
At each position, only two choices matter: extend the best subarray ending at
the previous position, or discard it and begin again at the current number.
If the previous running sum hurts the result, carrying it forward has no
benefit.

Initializing from nums[0], rather than zero, is important because the answer
for an all-negative array must be its least negative element—not an empty
subarray.
"""

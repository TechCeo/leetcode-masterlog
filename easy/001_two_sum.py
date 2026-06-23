"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices of
the two numbers that add up to target.

Each input has exactly one solution, and the same element cannot be used
twice. The answer may be returned in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Store each value's index while looking for its complement.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index

        return []


if __name__ == "__main__":
    sol = Solution()

    test(sol.twoSum, [2, 7, 11, 15], 9, [0, 1], "Test 1 - Basic pair")
    test(sol.twoSum, [3, 2, 4], 6, [1, 2], "Test 2 - Non-adjacent pair")
    test(sol.twoSum, [3, 3], 6, [0, 1], "Test 3 - Duplicate values")
    test(sol.twoSum, [-3, 4, 3, 90], 0, [0, 2], "Test 4 - Negative value")


"""
Reflection:
The brute-force approach compares every pair and takes O(n^2) time. A hash
map lets us ask whether target - number has already appeared in O(1) average
time.

We check for the complement before storing the current number. This prevents
one element from matching with itself while still allowing two equal values,
such as [3, 3], to form the answer.
"""

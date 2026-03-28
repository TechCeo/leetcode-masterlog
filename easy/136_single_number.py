"""
136. Single Number
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Bit Manipulation using XOR.
        
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Only one integer used for tracking the result.
        """
        res = 0
        for num in nums:
            # XOR logic: 
            # a ^ 0 = a
            # a ^ a = 0
            # Order doesn't matter (commutative/associative)
            res ^= num
        return res

if __name__ == "__main__":
    sol = Solution()

    test(sol.singleNumber, [2, 2, 1], 1, "Example 1")
    test(sol.singleNumber, [4, 1, 2, 1, 2], 4, "Example 2")
    test(sol.singleNumber, [1], 1, "Single Element")
    test(sol.singleNumber, [7, 6, 6, 7, 8], 8, "Custom Test Case")
"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, return the largest product of a contiguous
non-empty subarray.

Example:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product.
"""

import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Track both maximum and minimum products ending at each position.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current_maximum = nums[0]
        current_minimum = nums[0]
        best_product = nums[0]

        for number in nums[1:]:
            previous_maximum = current_maximum
            previous_minimum = current_minimum

            current_maximum = max(
                number,
                number * previous_maximum,
                number * previous_minimum,
            )
            current_minimum = min(
                number,
                number * previous_maximum,
                number * previous_minimum,
            )
            best_product = max(best_product, current_maximum)

        return best_product


if __name__ == "__main__":
    sol = Solution()

    test(sol.maxProduct, [2, 3, -2, 4], 6, "Test 1 - Positive best product")
    test(sol.maxProduct, [-2, 0, -1], 0, "Test 2 - Zero resets product")
    test(sol.maxProduct, [-2, 3, -4], 24, "Test 3 - Two negative values")
    test(sol.maxProduct, [-2], -2, "Test 4 - Single negative value")
    test(sol.maxProduct, [0, 2], 2, "Test 5 - Start after zero")


"""
Reflection:
Maximum product is similar to maximum subarray sum, except multiplication by
a negative number swaps the roles of large and small products. A very negative
minimum can become the next maximum, so both extremes must be carried forward.

Including the current number by itself in each comparison naturally starts a
new subarray after a zero or whenever the previous products are unhelpful.
Using temporary previous values prevents one updated extreme from incorrectly
influencing the other during the same iteration.
"""

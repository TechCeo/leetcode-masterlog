"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given a sorted array of unique integers that has been rotated between 1 and n
times, return its minimum element. The algorithm must run in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1
"""

import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Compare the middle value with the right boundary to locate the pivot.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # The minimum must be strictly to the right of middle.
                left = middle + 1
            else:
                # Middle could itself be the minimum, so keep it.
                right = middle

        return nums[left]


if __name__ == "__main__":
    sol = Solution()

    test(sol.findMin, [3, 4, 5, 1, 2], 1, "Test 1 - Rotated array")
    test(sol.findMin, [4, 5, 6, 7, 0, 1, 2], 0, "Test 2 - Larger rotation")
    test(sol.findMin, [11, 13, 15, 17], 11, "Test 3 - Sorted array")
    test(sol.findMin, [2, 1], 1, "Test 4 - Two elements")
    test(sol.findMin, [1], 1, "Test 5 - Single element")


"""
Reflection:
The final element is a useful reference because it belongs to the sorted
right-hand portion containing the minimum. If nums[middle] is greater than
nums[right], middle lies before the rotation point and can be discarded.
Otherwise, the minimum is at middle or somewhere to its left.

Using left < right lets both pointers converge directly on the minimum. When
the array is already sorted, the same comparisons steadily move right toward
the first element without requiring a separate special case.
"""

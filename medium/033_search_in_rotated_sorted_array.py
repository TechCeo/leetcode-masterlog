"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Given a sorted array of unique integers that may have been rotated, return the
index of target. Return -1 when target is absent. The algorithm must run in
O(log n) time.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Use binary search, choosing the sorted half at each step.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                # The left half is sorted.
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                # The right half is sorted.
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.search,
        [4, 5, 6, 7, 0, 1, 2],
        0,
        4,
        "Test 1 - Target after rotation",
    )
    test(
        sol.search,
        [4, 5, 6, 7, 0, 1, 2],
        3,
        -1,
        "Test 2 - Missing target",
    )
    test(sol.search, [1], 1, 0, "Test 3 - Single element found")
    test(sol.search, [1, 3], 3, 1, "Test 4 - Two elements")
    test(sol.search, [1, 2, 3, 4], 3, 2, "Test 5 - Not rotated")


"""
Reflection:
Rotation removes the guarantee that the whole search range is sorted, but at
least one half around the middle is always sorted. We identify that half and
check whether the target falls inside its boundaries. If it does, we keep it;
otherwise, we discard it.

Every decision removes half of the remaining range, preserving binary
search's O(log n) time without first locating the rotation point.
"""

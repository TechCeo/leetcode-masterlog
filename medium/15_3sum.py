"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that:
- i != j != k
- nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort + Two Pointers

        Time Complexity: O(n^2)
        Space Complexity: O(1) (excluding output)
        """
        nums.sort()
        n = len(nums)
        result = []

        for idx, num in enumerate(nums):
            # Skip duplicates for first element
            if idx and num == nums[idx - 1]:
                continue

            first = idx
            mid = idx + 1
            last = n - 1

            while mid < last:
                total = nums[first] + nums[mid] + nums[last]

                if total == 0:
                    result.append([nums[first], nums[mid], nums[last]])
                    mid += 1
                    last -= 1

                    # Skip duplicates for mid pointer
                    while mid < last and nums[mid] == nums[mid - 1]:
                        mid += 1

                elif total < 0:
                    mid += 1
                else:
                    last -= 1

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.threeSum,
         [-1,0,1,2,-1,-4],
         [[-1,-1,2],[-1,0,1]],
         "Example 1")

    test(sol.threeSum,
         [],
         [],
         "Empty Array")

    test(sol.threeSum,
         [0],
         [],
         "Single Element")

    test(sol.threeSum,
         [0,0,0],
         [[0,0,0]],
         "All Zeros")

    test(sol.threeSum,
         [-2,0,1,1,2],
         [[-2,0,2],[-2,1,1]],
         "Duplicates Handling")


"""
Reflection:
This problem builds directly on the two-pointer pattern from Two Sum II.

The key additions:
- Sorting to enable two-pointer traversal
- Skipping duplicates to ensure unique triplets

The tricky part is duplicate handling — especially after finding a valid triplet.
Missing that leads to repeated results, which is a common pitfall.

A great example of combining sorting + two pointers + careful edge handling.
"""
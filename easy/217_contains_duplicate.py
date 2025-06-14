"""
Problem 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Examples:
Input: [1,2,3,1]   → Output: True
Input: [1,2,3,4]   → Output: False
Input: [1,1,1,3,3,4,3,2,4,2] → Output: True

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


# Brute-force solution
class BruteForce:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time: O(n^2) – Compare each element with all others.
        Space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Optimal solution using a set
class HashSetSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time: O(n) – Single pass with constant-time set lookups.
        Space: O(n) – At most n elements in the set.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    print("\nBrute Force Solution:")
    bf = BruteForce()
    test(bf.containsDuplicate, [1, 2, 3, 1], True, "Test 1")
    test(bf.containsDuplicate, [1, 2, 3, 4], False, "Test 2")
    test(bf.containsDuplicate, [1], False, "Edge Case")

    print("\n--------------------------------------------------")
    print("Hash Set Optimized Solution:")
    opt = HashSetSolution()
    test(opt.containsDuplicate, [1, 2, 3, 1], True, "Test 1")
    test(opt.containsDuplicate, [1, 2, 3, 4], False, "Test 2")
    test(opt.containsDuplicate, [1], False, "Edge Case")

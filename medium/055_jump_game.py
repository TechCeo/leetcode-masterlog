"""
Problem 55: Jump Game
https://leetcode.com/problems/jump-game/

Given an integer array nums where each nums[i] represents the maximum jump
length from index i, return True if you can reach the last index.

Example:
Input: nums = [2,3,1,1,4]
Output: True
"""

from typing import List
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Track the farthest index reachable while scanning from left to right.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        farthest_reachable = 0

        for index, jump_length in enumerate(nums):
            if index > farthest_reachable:
                return False

            farthest_reachable = max(farthest_reachable, index + jump_length)

            if farthest_reachable >= len(nums) - 1:
                return True

        return True


if __name__ == "__main__":
    sol = Solution()

    test(sol.canJump, [2, 3, 1, 1, 4], True, "Test 1 - Can reach the end")
    test(sol.canJump, [3, 2, 1, 0, 4], False, "Test 2 - Stuck before the end")
    test(sol.canJump, [0], True, "Test 3 - Already at the end")
    test(sol.canJump, [2, 0, 0], True, "Test 4 - Exact jump covers the end")
    test(sol.canJump, [1, 0, 1, 0], False, "Test 5 - Gap after zero")

"""
Reflection:
This problem sits in the dynamic programming family because each index can be
viewed as reachable or not based on earlier reachable positions. The greedy
version compresses that DP state into one value: the farthest index we can
reach so far. If our scan ever moves beyond that boundary, no previous jump can
land on the current index, so the end is impossible to reach. This keeps the
same reachability idea while avoiding an O(n) DP array.
"""

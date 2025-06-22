"""
42. Trapping Rain Water

You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the amount of water that can be trapped after raining.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Constraints:
- 1 <= height.length <= 1000
- 0 <= height[i] <= 1000
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

from typing import List
from utils.test_utils import test

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time Complexity: O(n) – We traverse the array once using two pointers.
        Space Complexity: O(1) – We use constant space for variables.
        """
        if not height:
            return 0

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped += max(0, right_max - height[right])

        return trapped

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.trap, [0,2,0,3,1,0,1,3,2,1], 9, "Test 1")
    test(sol.trap, [4,2,0,3,2,5], 9, "Test 2")
    test(sol.trap, [1,0,1], 1, "Test 3")
    test(sol.trap, [0,1,2,3], 0, "Test 4")
    test(sol.trap, [3,2,1,0], 0, "Test 5")
    test(sol.trap, [2,0,2], 2, "Test 6")

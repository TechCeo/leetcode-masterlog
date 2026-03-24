"""
11. Container With Most Water

Given an integer array heights where heights[i] represents the height of the ith bar,
choose two bars such that together they form a container that holds the maximum water.

Return the maximum area of water a container can store.
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Two Pointers Approach

        Start with the widest container and shrink inward.
        Always move the pointer at the shorter height.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left

            h_left = heights[left]
            h_right = heights[right]

            if h_left < h_right:
                current_area = h_left * width
                left += 1
            else:
                current_area = h_right * width
                right -= 1

            if current_area > max_area:
                max_area = current_area

        return max_area


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.maxArea,
         [1,8,6,2,5,4,8,3,7],
         49,
         "Example 1")

    test(sol.maxArea,
         [1,1],
         1,
         "Two Elements")

    test(sol.maxArea,
         [4,3,2,1,4],
         16,
         "Symmetric Heights")

    test(sol.maxArea,
         [1,2,1],
         2,
         "Small Peak")

    test(sol.maxArea,
         [2,3,10,5,7,8,9],
         36,
         "Peak Inside")


"""
Reflection:
At first glance, this problem feels like brute force (checking all pairs),
but that would be O(n^2).

The key realization is:
The area is limited by the shorter height.

So instead of exploring all pairs, we:
- Start with the widest container
- Move inward strategically

Moving the taller pointer is useless because:
- Width decreases
- Height constraint does not improve

This greedy pointer movement is the core insight.
"""
"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is formed by bars [5, 6] with area = 10.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Use a monotonic stack to track indices of bars in increasing order.
        When we encounter a bar shorter than the top of stack:
        - Pop from stack and calculate area with that bar's height
        - The width extends from current index to the popped bar's position
        
        Time Complexity: O(n) – Each bar is pushed and popped once
        Space Complexity: O(n) – Stack stores indices
        """
        stack = []  # Stack stores indices
        max_area = 0
        
        for i in range(len(heights)):
            # Pop bars taller than current bar and calculate areas
            while stack and heights[stack[-1]] > heights[i]:
                h_idx = stack.pop()
                h = heights[h_idx]
                # Width: from current position to left boundary
                # Left boundary: index after the previous bar in stack (or -1)
                w = i if not stack else i - stack[-1] - 1
                area = h * w
                max_area = max(max_area, area)
            
            stack.append(i)
        
        # Process remaining bars in stack
        while stack:
            h_idx = stack.pop()
            h = heights[h_idx]
            # Width extends to the end of array
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = h * w
            max_area = max(max_area, area)
        
        return max_area


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example test cases
    test(sol.largestRectangleArea, [2,1,5,6,2,3], 10, "Test 1 - Example")
    test(sol.largestRectangleArea, [2,4], 4, "Test 2 - Example")
    
    # Edge cases
    test(sol.largestRectangleArea, [0], 0, "Test 3 - Single zero")
    test(sol.largestRectangleArea, [5], 5, "Test 4 - Single bar")
    test(sol.largestRectangleArea, [1,2,3,4,5], 9, "Test 5 - Increasing")
    test(sol.largestRectangleArea, [5,4,3,2,1], 9, "Test 6 - Decreasing")
    
    # Mixed cases
    test(sol.largestRectangleArea, [2,0,2], 2, "Test 7 - Valley")
    test(sol.largestRectangleArea, [0,2,0,3,1,0,1,3,2,1], 4, "Test 8 - Multiple peaks")
    test(sol.largestRectangleArea, [4,2,0,3,2,5], 6, "Test 9 - Complex")
    test(sol.largestRectangleArea, [6,6,6], 18, "Test 10 - All same height")

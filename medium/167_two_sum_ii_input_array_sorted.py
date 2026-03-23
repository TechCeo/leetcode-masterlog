"""
167. Two Sum II - Input Array Is Sorted

Given a sorted array of integers (non-decreasing),
return the 1-indexed positions of two numbers such that they add up to target.

Constraints:
- Exactly one solution exists
- Must use O(1) extra space

Example:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two Pointer Approach

        Since the array is sorted:
        - Start with left at beginning, right at end
        - If sum is too small → move left forward
        - If sum is too large → move right backward

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []  # guaranteed not to reach here


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.twoSum,
         [1, 2, 3, 4],
         3,
         [1, 2],
         "Example 1")

    test(sol.twoSum,
         [2, 7, 11, 15],
         9,
         [1, 2],
         "Classic Case")

    test(sol.twoSum,
        [1, 3, 4, 5, 7, 10, 11],
        9,
        [3, 4],
        "Middle Pair")

    test(sol.twoSum,
         [-3, -1, 0, 2, 4, 5],
        1,
        [1, 5],
        "With Negatives")


"""
Reflection:
This problem is a perfect demonstration of how sorting unlocks powerful optimizations.

Instead of using a hash map (like Two Sum I), we leverage the sorted property
to move pointers intelligently and achieve O(1) space.

A strong reminder: always check if input constraints (like sorted order)
can simplify the problem dramatically.
"""
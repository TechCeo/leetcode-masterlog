"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4  (sequence: [1,2,3,4])
"""

from typing import List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Use a set for O(1) lookups.

        Only start counting when we find the beginning of a sequence
        (i.e., num - 1 is NOT in the set).

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Only start counting if it's the start of a sequence
            if (num - 1) not in nums_set:
                run_len = 1

                while (num + run_len) in nums_set:
                    run_len += 1

                longest = max(longest, run_len)

        return longest


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.longestConsecutive,
         [100, 4, 200, 1, 3, 2],
         4,
         "Example 1")

    test(sol.longestConsecutive,
         [0,3,7,2,5,8,4,6,0,1],
         9,
         "Example 2")

    test(sol.longestConsecutive,
         [],
         0,
         "Empty Array")

    test(sol.longestConsecutive,
         [1,2,0,1],
         3,
         "Duplicates Case")


"""
💭 Reflection:
This problem is a great example of reducing time complexity using a hash set.

The key optimization is avoiding redundant work:
instead of checking every number as a potential sequence,
we only start when we detect the beginning of a sequence.

That single condition (num - 1 not in set) is what brings the solution down to O(n).
"""
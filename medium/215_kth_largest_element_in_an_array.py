"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element
in the array. It is the kth element in sorted order, not the kth distinct
element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""

import os
import random
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Use Quickselect to place only the element we need.

        Time Complexity: O(n) average, O(n^2) worst case
        Space Complexity: O(1)
        """
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_index = self._partition(nums, left, right, pivot_index)

            if pivot_index == target:
                return nums[pivot_index]
            if pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        raise ValueError("k must be between 1 and the length of nums")

    def _partition(
        self,
        nums: List[int],
        left: int,
        right: int,
        pivot_index: int,
    ) -> int:
        """Move values smaller than the pivot to its left side."""
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for index in range(left, right):
            if nums[index] < pivot_value:
                nums[store_index], nums[index] = nums[index], nums[store_index]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.findKthLargest,
        [3, 2, 1, 5, 6, 4],
        2,
        5,
        "Test 1 - Second largest",
    )
    test(
        sol.findKthLargest,
        [3, 2, 3, 1, 2, 4, 5, 5, 6],
        4,
        4,
        "Test 2 - Duplicates",
    )
    test(
        sol.findKthLargest,
        [-1, -4, -2, -3],
        1,
        -1,
        "Test 3 - Negative values",
    )
    test(
        sol.findKthLargest,
        [7],
        1,
        7,
        "Test 4 - Single element",
    )


"""
Reflection:
The kth largest value has index len(nums) - k when the array is viewed in
ascending order. Quickselect uses the same partition step as Quicksort, but
continues into only the side containing that target index.

After partitioning, the pivot is in its final sorted position. Everything to
its left is smaller, so comparing the pivot index with the target tells us
which half can be discarded. Randomizing the pivot makes O(n) the expected
running time, although a consistently unlucky pivot sequence can still take
O(n^2). The algorithm rearranges nums in place.

Another strong solution is to maintain a min-heap of size k. After scanning
the array, the heap contains the k largest values, and its root is the kth
largest. That approach takes O(n log k) time and O(k) extra space. It provides
more predictable performance and is especially useful when k is small or the
values arrive as a stream.

We chose Quickselect because this problem gives us the complete mutable array.
It has better expected time, O(n), and uses O(1) extra space. The trade-off is
that it modifies the input and has an O(n^2) worst case, whereas the heap does
not need to rearrange the array and avoids that unlucky-pivot behavior.
"""

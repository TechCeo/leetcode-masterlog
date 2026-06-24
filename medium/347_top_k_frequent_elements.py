"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent
elements. The answer may be returned in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

import heapq
import os
import sys
from collections import Counter
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.test_utils import test


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Maintain a min-heap containing the k highest frequencies seen so far.

        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        frequencies = Counter(nums)
        min_heap = []

        for number, frequency in frequencies.items():
            heapq.heappush(min_heap, (frequency, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # LeetCode accepts any order; sorting keeps local test output stable.
        return sorted(number for _, number in min_heap)


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.topKFrequent,
        [1, 1, 1, 2, 2, 3],
        2,
        [1, 2],
        "Test 1 - Two most frequent",
    )
    test(sol.topKFrequent, [1], 1, [1], "Test 2 - Single element")
    test(
        sol.topKFrequent,
        [4, 4, 4, 6, 6, 7, 7, 7, 7],
        2,
        [4, 7],
        "Test 3 - Different frequencies",
    )
    test(
        sol.topKFrequent,
        [-1, -1, -2, -2, -2, 3],
        1,
        [-2],
        "Test 4 - Negative values",
    )


"""
Reflection:
The frequency map reduces the array to one entry per distinct value. A
min-heap of size k then keeps only the strongest candidates: whenever its size
exceeds k, removing the root discards the lowest frequency seen so far. Once
all frequencies have been processed, every remaining value belongs in the
answer.

A bucket-sort solution can achieve O(n) time by using frequencies as indices,
but it allocates buckets based on the input length. The heap approach takes
O(n log k) time and is especially attractive when k is small because it keeps
only k candidates in the selection structure. The Counter still requires
O(n) space in the worst case.
"""

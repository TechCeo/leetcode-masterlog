"""
1726. Tuple with Same Product
Link: https://leetcode.com/problems/tuple-with-same-product/

Given an array of distinct positive integers, return the number of tuples (a, b, c, d)
such that a * b = c * d and a, b, c, d are distinct.

Time Complexity: O(n^2)
    - We check all unique pairs, which is n(n-1)/2 = O(n^2)
Space Complexity: O(n)
    - We store frequency of products in a hashmap
"""

from typing import List
from collections import defaultdict
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_map[prod] += 1

        result = 0
        for count in product_map.values():
            if count > 1:
                result += count * (count - 1) * 4  # Each combination yields 8 permutations / 2 = 4 valid tuples

        return result


# Test Cases
from utils.test_utils import test

sol = Solution()
test(sol.tupleSameProduct, [2, 3, 4, 6], 8, "Test 1")
test(sol.tupleSameProduct, [1, 2, 4, 5, 10], 16, "Test 2")
test(sol.tupleSameProduct, [1, 2, 3, 4], 0, "Test 3")
test(sol.tupleSameProduct, [1], 0, "Edge Case - Single Element")

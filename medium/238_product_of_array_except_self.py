"""
Problem 238: Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
You must solve it without using division and in O(n) time.

Input: [1,2,3,4]       → Output: [24,12,8,6]
Input: [-1,1,0,-3,3]   → Output: [0,0,9,0,0]
--------------------------------------------------
## My Thought Process

1. My first instinct was to try a brute-force approach — for each index, multiply all other elements.
2. I realized quickly that this results in O(n²) time complexity, which is too slow for large input sizes.
3. I then explored prefix and suffix strategies to eliminate the nested loop while maintaining the product logic.

"""
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


# Brute-force solution
class BruteForce:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n²) – For each element, we loop through the array again.
        Space: O(n) – Output array of size n.
        """
        result = [1] * len(nums)
        for index in range(len(nums)):
            for j in range(len(nums)):
                if index == j:
                    continue
                result[index] *= nums[j]
        return result


"""
Optimized Approach
Instead of recalculating every product from scratch, im breaking the computation into two passes:
Forward pass: Compute prefix product for each index
Backward pass: Multiply by the suffix product
"""
# Optimized solution
class PrefixSuffixOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n) – Single forward and backward pass.
        Space: O(1) extra – We reuse the output array (excluding the result itself).
        """
        result = [1] * len(nums)

        # compute prefix product
        pre = 1
        for index, num in enumerate(nums):
            result[index] = pre
            pre = pre * num
            
        # compute post fix
        post = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= post
            post = post * nums[index]

        return result
    
    
if __name__ == "__main__":
    print("\n Brute Force Solution:")
    bf = BruteForce()
    test(bf.productExceptSelf, [1, 2, 3, 4], [24, 12, 8, 6], "Test 1")
    test(bf.productExceptSelf, [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "Test 2")
    
    print("\n Optimized Solution:")
    sol = PrefixSuffixOptimized()
    test(sol.productExceptSelf, [1, 2, 3, 4], [24, 12, 8, 6], "Test 1")
    test(sol.productExceptSelf, [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "Test 2")

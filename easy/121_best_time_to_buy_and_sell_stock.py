"""
Problem 121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
Choose one day to buy and a different day in the future to sell. Return the maximum profit.
If no transaction is possible, return 0.

Examples:
Input: [10,1,5,6,7,1] → Output: 6 (Buy at 1, sell at 7)
Input: [10,8,7,5,2]   → Output: 0 (No profit possible)

Constraints:
- 1 <= prices.length <= 100
- 0 <= prices[i] <= 100
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class TwoPointerGreedy:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        profit = 0
        left = 0  # Buy index

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])

        return profit


if __name__ == "__main__":
    print("\nTwo-Pointer Greedy Solution:")
    sol = TwoPointerGreedy()
    test(sol.maxProfit, [10,1,5,6,7,1], 6, "Test 1")
    test(sol.maxProfit, [10,8,7,5,2], 0, "Test 2")
    test(sol.maxProfit, [2,1,2,1,0,1,2], 2, "Test 3")


"""
Reflection:
This problem was fairly straightforward. I used a two-pointer strategy:
track the lowest price as you iterate, and calculate potential profit at each step.
Update profit only when you find a better one. No extra space, and just one loop.
"""

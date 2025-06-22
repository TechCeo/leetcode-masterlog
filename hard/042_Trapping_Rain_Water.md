# Reflection: 042. Trapping Rain Water

## Problem Summary

We are given an array `height` representing an elevation map where the width of each bar is 1. The goal is to compute how much water can be trapped after raining.

---

## Solution Approach

To solve this efficiently, I employed the **two-pointer technique**. The idea hinges on the fact that water trapped at a position is determined by the smaller of the maximum heights to its left and right.

### Algorithm Breakdown

- Initialize two pointers: `left` at 0 and `right` at the end of the array.
- Track `left_max` and `right_max` which represent the highest bars seen so far from the left and right, respectively.
- While `left < right`:
  - If `left_max < right_max`, we move the left pointer one step right. If the current height is less than `left_max`, it contributes to trapped water.
  - Otherwise, move the right pointer one step left, and use the same logic in the opposite direction.
- Accumulate trapped water into a variable `trapped`.

This ensures that every element is processed only once, providing an optimal linear-time solution.

---

## Time and Space Complexity

- **Time Complexity**: `O(n)` – Each element is visited at most once.
- **Space Complexity**: `O(1)` – We use only a fixed number of pointers and counters, no extra data structures.

---

## Final Thoughts

This problem is a great illustration of how two-pointer techniques can elegantly replace more naive approaches that require additional memory or nested loops. It’s efficient, readable, and avoids unnecessary complexity.

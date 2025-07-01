# 036. Valid Sudoku — Reflection

🔗 [View on LeetCode](https://leetcode.com/problems/valid-sudoku/)

You are given a 9 x 9 Sudoku board...


## Problem summary:
Validate a 9x9 Sudoku board to ensure that no number is repeated in any row, column, or 3x3 sub-box.

## Initial Approach (Three Separate Loops)
I started with a clear and explicit method:

Loop 1: Validate rows by checking for duplicates using a set.

Loop 2: Validate columns using a similar technique.

Loop 3: Manually iterate over each of the 9 sub-boxes using index arithmetic and validate for duplicates.

## Time Complexity:
O(9²) = O(81) — Each cell is visited once per loop (three loops in total, but constants are dropped in Big-O).

Space Complexity:
O(9 × 3) = O(1) — Three sets per iteration, but since the board size is fixed at 9x9, this is constant space.

## Trade-Off:
- Easy to follow and debug.

- Redundant logic and less elegant.

- Requires three full traversals of the board.

Optimized Approach (Single Traversal with Hash Sets)
In the improved version:

- I used defaultdict(set) to track numbers for rows, columns, and sub-boxes.

- I traversed the board only once.

- Sub-boxes are indexed using (i // 3, j // 3) for a clean and intuitive mapping.

## Time Complexity:
O(81) = O(1) — Still constant time due to the fixed size (9x9) of the board.

## Space Complexity:
O(81) = O(1) — At most 81 entries across the row, column, and box dictionaries; still constant.

## Benefits:
- Cleaner logic — all checks are consolidated in one loop.

- Less code and improved readability.

- Early exits on invalid conditions, making it slightly more efficient in practice.

## Trade-Off:
- Improved maintainability and elegance.

- Reuses logic across dimensions (row, col, box) instead of separating them.

- Slightly more abstract due to the use of defaultdict and tuple keys.

## Final Thoughts
This problem reinforced the value of:

- Clean data structure choices (defaultdict(set)).

- One-pass logic when possible for clarity and performance.

- Viewing 2D structures like sub-boxes through coordinate transformations.

- By refactoring the code to be more concise and data-driven, the solution becomes not just faster in execution, but stronger in design — a key goal in writing production-quality code.


"""
Problem 124: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of connected nodes where each pair of
adjacent nodes has an edge connecting them. A node may appear at most once.
The path does not need to pass through the root.

Return the maximum path sum of any non-empty path.

Examples:
Input: root = [1,2,3]
Output: 6

Input: root = [-10,9,20,None,None,15,7]
Output: 42
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import TreeNode, build_tree_from_list
from utils.test_utils import test


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Postorder DFS approach.

        For each node:
        - Compute the best one-sided path that can be extended by its parent.
        - Use both positive child paths to evaluate a complete path through
          the current node.
        - Track the best complete path globally.

        Time Complexity: O(n) - Every node is visited once.
        Space Complexity: O(h) - Recursive stack for tree height h.
        """
        max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, path_sum)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(max_sum)


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.maxPathSum,
        build_tree_from_list([1, 2, 3]),
        6,
        "Test 1 - Path through root",
    )
    test(
        sol.maxPathSum,
        build_tree_from_list([-10, 9, 20, None, None, 15, 7]),
        42,
        "Test 2 - Path below root",
    )
    test(
        sol.maxPathSum,
        build_tree_from_list([-3]),
        -3,
        "Test 3 - Single negative node",
    )
    test(
        sol.maxPathSum,
        build_tree_from_list([2, -1]),
        2,
        "Test 4 - Ignore negative branch",
    )
    test(
        sol.maxPathSum,
        build_tree_from_list([-2, -1]),
        -1,
        "Test 5 - All negative values",
    )

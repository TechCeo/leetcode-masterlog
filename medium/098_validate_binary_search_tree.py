"""
Problem 98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree.

A valid BST has the following properties:
- Every node in the left subtree is strictly less than the current node.
- Every node in the right subtree is strictly greater than the current node.
- Both subtrees must also be valid binary search trees.

Examples:
Input: root = [2,1,3]
Output: True

Input: root = [5,1,4,None,None,3,6]
Output: False
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import TreeNode, build_tree_from_list
from utils.test_utils import test


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS with lower and upper bounds.

        Each node must satisfy every ancestor constraint, not only the
        relationship with its direct parent.

        Time Complexity: O(n) - Every node is visited once.
        Space Complexity: O(h) - Recursive stack for tree height h.
        """
        def validate(
            node: Optional[TreeNode],
            lower: float,
            upper: float,
        ) -> bool:
            if not node:
                return True

            if not lower < node.val < upper:
                return False

            return (
                validate(node.left, lower, node.val)
                and validate(node.right, node.val, upper)
            )

        return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.isValidBST,
        build_tree_from_list([2, 1, 3]),
        True,
        "Test 1 - Valid BST",
    )
    test(
        sol.isValidBST,
        build_tree_from_list([5, 1, 4, None, None, 3, 6]),
        False,
        "Test 2 - Invalid right subtree",
    )
    test(
        sol.isValidBST,
        build_tree_from_list([5, 4, 6, None, None, 3, 7]),
        False,
        "Test 3 - Violates ancestor bound",
    )
    test(
        sol.isValidBST,
        build_tree_from_list([2, 2, 3]),
        False,
        "Test 4 - Duplicate value",
    )
    test(sol.isValidBST, build_tree_from_list([]), True, "Test 5 - Empty tree")

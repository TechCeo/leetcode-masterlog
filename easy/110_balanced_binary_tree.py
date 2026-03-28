"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A binary tree is balanced if:
For every node, the height difference between left and right subtrees is ≤ 1.
"""

from typing import Optional
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import build_tree_from_list
from utils.test_utils import test


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        DFS returning:
        - whether subtree is balanced
        - height of subtree

        Time Complexity: O(n)
        Space Complexity: O(h)
        """

        def dfs(node):
            if not node:
                return True, 0

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            return balanced, 1 + max(left_height, right_height)

        return dfs(root)[0]


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.isBalanced,
         build_tree_from_list([3,9,20,None,None,15,7]),
         True,
         "Balanced Tree")

    test(sol.isBalanced,
         build_tree_from_list([1,2,2,3,3,None,None,4,4]),
         False,
         "Unbalanced Tree")

    test(sol.isBalanced,
         build_tree_from_list([1]),
         True,
         "Single Node")

    test(sol.isBalanced,
         build_tree_from_list([]),
         True,
         "Empty Tree")


"""
💭 Reflection:
This problem is a natural extension of the diameter problem.

Instead of just computing heights, we also track whether subtrees are balanced.

The key optimization:
- Combine height calculation and balance checking in ONE traversal

A naive approach might recompute heights repeatedly → O(n^2),
but this bottom-up approach keeps it O(n).

Return multiple values from DFS to avoid redundant work.
"""
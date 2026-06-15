"""
Problem 236: Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree and two nodes p and q, return their lowest common ancestor.

The lowest common ancestor is the lowest node in the tree that has both p and q
as descendants. A node is allowed to be a descendant of itself.

Examples:
Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
Output: 3

Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
Output: 5
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import TreeNode, build_tree_from_list
from utils.test_utils import test


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> Optional[TreeNode]:
        """
        Recursive DFS approach.

        If p and q are found in different subtrees, the current node is their
        lowest common ancestor. If both are below one side, that side's result
        is passed upward.

        Time Complexity: O(n) - Every node may be visited once.
        Space Complexity: O(h) - Recursive stack for tree height h.
        """
        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    node_5 = root.left
    node_1 = root.right
    node_7 = root.left.right.left
    node_4 = root.left.right.right

    test(
        sol.lowestCommonAncestor,
        root,
        node_5,
        node_1,
        root,
        "Test 1 - Nodes in different subtrees",
    )
    test(
        sol.lowestCommonAncestor,
        root,
        node_5,
        node_4,
        node_5,
        "Test 2 - Ancestor is one target",
    )
    test(
        sol.lowestCommonAncestor,
        root,
        node_7,
        node_4,
        root.left.right,
        "Test 3 - Sibling nodes",
    )

    single = build_tree_from_list([1])
    test(
        sol.lowestCommonAncestor,
        single,
        single,
        single,
        single,
        "Test 4 - Same node",
    )

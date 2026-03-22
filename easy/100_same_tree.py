"""
100. Same Tree

Given the roots of two binary trees p and q, return true if they are the same,
and false otherwise.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: True
"""

from typing import Optional
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.binary_tree_utils import build_tree_from_list
from utils.test_utils import test


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: Optional[int]):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive DFS comparison

        Time Complexity: O(n)
        Space Complexity: O(h) recursion stack
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(
        sol.isSameTree,
        build_tree_from_list([1, 2, 3]),
        build_tree_from_list([1, 2, 3]),
        True,
        "Same Trees"
    )

    test(
        sol.isSameTree,
        build_tree_from_list([1, 2]),
        build_tree_from_list([1, None, 2]),
        False,
        "Different Structure"
    )

    test(
        sol.isSameTree,
        build_tree_from_list([1, 2, 1]),
        build_tree_from_list([1, 1, 2]),
        False,
        "Different Values"
    )

    test(
        sol.isSameTree,
        build_tree_from_list([]),
        build_tree_from_list([]),
        True,
        "Empty Trees"
    )


"""
Reflection:
This is a fundamental recursion problem on trees.

The key idea is to compare both structure and values simultaneously.
At each node:
- Both must be None → valid
- One is None → invalid
- Values differ → invalid

Otherwise, recurse on left and right.

A great reminder that many tree problems boil down to breaking the problem
into identical subproblems and trusting recursion to handle the structure cleanly.
"""
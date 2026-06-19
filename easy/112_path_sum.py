"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals
targetSum.

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: True
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        DFS with remaining sum

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return False

        remaining = targetSum - root.val
        if not root.left and not root.right:
            return remaining == 0

        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.hasPathSum,
         build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
         22,
         True,
         "Example Path Exists")

    test(sol.hasPathSum,
         build_tree_from_list([1, 2, 3]),
         5,
         False,
         "No Valid Path")

    test(sol.hasPathSum,
         build_tree_from_list([]),
         0,
         False,
         "Empty Tree")

    test(sol.hasPathSum,
         build_tree_from_list([1, 2]),
         1,
         False,
         "Root Alone Is Not Leaf")

    test(sol.hasPathSum,
         build_tree_from_list([-2, None, -3]),
         -5,
         True,
         "Negative Values")


"""
Reflection:
Path Sum is a root-to-leaf DFS problem.

The important detail is that a path only counts when it ends at a leaf.
That means matching the target at an internal node is not enough.

Passing the remaining sum down the tree keeps the recursion clean:
- subtract the current node
- if this is a leaf, check whether the remainder is zero
- otherwise keep searching left and right
"""

"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself.

Example:
Input: root = [1,2,2,3,4,4,3]
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive mirror comparison

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return True

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return (
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.isSymmetric,
         build_tree_from_list([1, 2, 2, 3, 4, 4, 3]),
         True,
         "Symmetric Tree")

    test(sol.isSymmetric,
         build_tree_from_list([1, 2, 2, None, 3, None, 3]),
         False,
         "Asymmetric Structure")

    test(sol.isSymmetric,
         build_tree_from_list([1, 2, 2, 2, None, 2]),
         False,
         "Asymmetric Shape")

    test(sol.isSymmetric,
         build_tree_from_list([]),
         True,
         "Empty Tree")


"""
Reflection:
This problem is very close to Same Tree, except the comparison crosses over.

Instead of comparing:
- left with left
- right with right

We compare:
- left subtree's left child with right subtree's right child
- left subtree's right child with right subtree's left child

That mirrored pairing is the whole trick.
"""

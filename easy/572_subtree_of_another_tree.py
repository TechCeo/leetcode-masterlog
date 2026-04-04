"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a 
subtree of root with the same structure and node values of subRoot and false otherwise.
"""

from typing import Optional
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import TreeNode, build_tree_from_list
from utils.test_utils import test

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Double Recursion Approach
        
        Time Complexity: O(n * m) - In worst case, we call isSameTree(m) for every node in root(n).
        Space Complexity: O(h) - Height of the taller tree.
        """
        
        if not root: 
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()

    # Case 1: subRoot exists
    t1 = build_tree_from_list([3, 4, 5, 1, 2])
    s1 = build_tree_from_list([4, 1, 2])
    test(sol.isSubtree, t1, s1, True, "Subtree exists")

    # Case 2: subRoot has extra children in main tree
    t2 = build_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
    s2 = build_tree_from_list([4, 1, 2])
    test(sol.isSubtree, t2, s2, False, "Structural mismatch at leaf")
"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST) and two nodes p and q, return their lowest common ancestor (LCA).
The LCA is the lowest node in the tree that has both p and q as descendants (including the possibility of being one of them).

Example:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Time Complexity: O(h), where h is the height of the BST.
Space Complexity: O(1) for iterative, or O(h) for recursive stack.
"""

from typing import Optional
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test
from utils.binary_tree_utils import TreeNode, build_tree_from_list

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Iterative approach using BST properties:
        - If both p and q are less than root, LCA lies in left subtree.
        - If both are greater, LCA lies in right subtree.
        - If they diverge or match root, root is the LCA.
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root  # Found LCA
        return None


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Helper tree
    root = build_tree_from_list([5,3,8,1,4,7,9,None,2])
    node3 = root.left  # 3
    node8 = root.right  # 8
    node4 = root.left.right  # 4

    test(sol.lowestCommonAncestor, root, node3, node8, root, "Test 1: LCA of 3 and 8")
    test(sol.lowestCommonAncestor, root, node3, node4, node3, "Test 2: LCA of 3 and 4")

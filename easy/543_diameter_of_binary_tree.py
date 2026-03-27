"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter.

The diameter is the length (number of edges) of the longest path between any two nodes.
The path does not necessarily pass through the root.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS + Height Calculation

        At each node:
        - Compute left height
        - Compute right height
        - Update diameter = left + right

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        max_path = [0]  # use list for mutability in recursion
        self.dfs(root, max_path)
        return max_path[0]

    def dfs(self, node: Optional[TreeNode], max_path) -> int:
        if not node:
            return 0

        left = self.dfs(node.left, max_path)
        right = self.dfs(node.right, max_path)

        # Diameter at this node = left height + right height
        max_path[0] = max(max_path[0], left + right)

        # Return height of subtree
        return max(left, right) + 1


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test(sol.diameterOfBinaryTree,
         build_tree_from_list([1, None, 2, 3, 4, 5]),
         3,
         "Example 1")

    test(sol.diameterOfBinaryTree,
         build_tree_from_list([1, 2, 3]),
         2,
         "Example 2")

    test(sol.diameterOfBinaryTree,
         build_tree_from_list([1]),
         0,
         "Single Node")

    test(sol.diameterOfBinaryTree,
         build_tree_from_list([]),
         0,
         "Empty Tree")


"""
💭 Reflection:
This problem looks like a "path" problem, but the key is realizing:

The longest path through a node = left subtree height + right subtree height.

So instead of explicitly tracking paths, we:
- Compute heights via DFS
- Update the best diameter at each node

This is a classic example of combining:
- Bottom-up recursion (heights)
- Global state tracking (diameter)

A very important tree DP pattern.
"""
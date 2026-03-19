"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its depth.

The depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example:
Input: root = [1,2,3,null,null,4]
Output: 3
"""

from collections import deque
from typing import Optional, List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test_tree
from utils.binary_tree_utils import build_tree_from_list



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: Optional[int]):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS Level Order Traversal

        We traverse the tree level by level.
        Each level processed increments depth.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level


# # Test Cases
# if __name__ == "__main__":
#     sol = Solution()

#     test_tree(sol.maxDepth, build_tree_from_list([1, 2, 3, None, None, 4]), 3, "Test 1")
#     test_tree(sol.maxDepth, build_tree_from_list([1]), 1, "Single Node")
#     test_tree(sol.maxDepth, build_tree_from_list([]), 0, "Empty Tree")
#     test_tree(sol.maxDepth, build_tree_from_list([1,2,3,4,5,6,7]), 3, "Full Tree")


"""
Reflection:
This is a classic binary tree problem that reinforces level-order traversal (BFS).
Instead of tracking paths explicitly, counting levels naturally gives the depth.

DFS would also work here, but BFS makes the concept of "levels" very intuitive.
Good reminder that sometimes the simplest traversal pattern is the cleanest solution.
"""
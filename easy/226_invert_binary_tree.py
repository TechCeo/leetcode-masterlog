"""
226. Invert Binary Tree

You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

Constraints:
- 0 <= The number of nodes in the tree <= 100.
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional, List
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from utils.test_utils import test
from utils.test_utils import test_tree
from utils.binary_tree_utils import build_tree_from_list

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: Optional[int]):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n) – We visit every node once.
        Space Complexity: O(n) – For the queue in the worst case (breadth of the tree).
        """
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test_tree(sol.invertTree, build_tree_from_list([1, 2, 3, 4, 5, 6, 7]), [1, 3, 2, 7, 6, 5, 4], "Test 1")
    test_tree(sol.invertTree, build_tree_from_list([3, 2, 1]), [3, 1, 2], "Test 2")
    test_tree(sol.invertTree, build_tree_from_list([]), [], "Test 3")




"""
Reflection:
This problem is essentially a tree traversal exercise where the key operation is to swap the left and right children of each node.
I chose to use an iterative Breadth-First Search (BFS) approach using a queue. This approach is easy to follow and avoids recursion stack limits.

Alternatively, a Depth-First Search (DFS) via recursion would work equally well, and might be preferred for its conciseness.

Key Insight:
- Swapping left and right nodes at each level doesn’t require maintaining additional structure — just a queue suffices.
- Ensuring you visit every node is enough to guarantee a full inversion of the tree.

Time Complexity: O(n) – We visit every node exactly once.
Space Complexity: O(n) – At worst, the queue stores all nodes at the last level of the tree (i.e., the tree’s breadth).
"""

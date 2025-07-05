"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

Time Complexity: O(n), where n is the number of nodes.
Space Complexity: O(n) for the queue used in BFS.

Approach: Breadth-First Search (BFS) using a queue.
"""

from collections import deque
from typing import Optional, List
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import TreeNode, build_tree_from_list
from utils.test_utils import test

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    test_tree_1 = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    test(sol.levelOrder, test_tree_1, [[1], [2, 3], [4, 5, 6, 7]], "Test 1: Full tree")

    test_tree_2 = build_tree_from_list([1])
    test(sol.levelOrder, test_tree_2, [[1]], "Test 2: Single node")

    test_tree_3 = build_tree_from_list([])
    test(sol.levelOrder, test_tree_3, [], "Test 3: Empty tree")

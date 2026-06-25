"""
Problem 261: Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges, return
True if these edges make up a valid tree.

A valid tree must satisfy two rules:
1. It has exactly n - 1 edges.
2. All nodes are connected with no cycles.

Examples:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: True

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: False
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Union-Find approach.

        A tree with n nodes must have exactly n - 1 edges. After that quick
        check, Union-Find lets us detect whether any edge creates a cycle.

        Time Complexity: O(n + e * α(n)) - α(n) is nearly constant.
        Space Complexity: O(n) - Parent and rank arrays.
        """
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.validTree,
        5,
        [[0, 1], [0, 2], [0, 3], [1, 4]],
        True,
        "Test 1 - Valid tree",
    )
    test(
        sol.validTree,
        5,
        [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
        False,
        "Test 2 - Cycle exists",
    )
    test(sol.validTree, 4, [[0, 1], [2, 3]], False, "Test 3 - Disconnected")
    test(sol.validTree, 1, [], True, "Test 4 - Single node")


"""
Reflection:
The key insight is that a tree is not just "no cycles" and not just
"connected"; it needs both. Checking for exactly n - 1 edges is a clean
shortcut because if an undirected graph has n - 1 edges and no cycle, it must
also be connected.

Union-Find is a great fit here because each edge asks the same question:
"Are these two nodes already connected?" If yes, adding the edge creates a
cycle. If no, we safely merge their components.
"""

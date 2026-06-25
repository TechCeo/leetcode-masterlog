"""
Problem 323: Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges, return
the number of connected components in the graph.

Examples:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""

from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union-Find approach.

        Start with n separate components. Every successful union merges two
        previously separate components, so we decrement the count.

        Time Complexity: O(n + e * α(n)) - α(n) is nearly constant.
        Space Complexity: O(n) - Parent and rank arrays.
        """
        parent = list(range(n))
        rank = [0] * n
        components = n

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
            if union(a, b):
                components -= 1

        return components


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.countComponents,
        5,
        [[0, 1], [1, 2], [3, 4]],
        2,
        "Test 1 - Two components",
    )
    test(
        sol.countComponents,
        5,
        [[0, 1], [1, 2], [2, 3], [3, 4]],
        1,
        "Test 2 - One connected graph",
    )
    test(sol.countComponents, 4, [], 4, "Test 3 - No edges")
    test(
        sol.countComponents,
        6,
        [[0, 1], [2, 3], [4, 5], [1, 2]],
        2,
        "Test 4 - Merge existing groups",
    )


"""
Reflection:
This problem is the counting cousin of Graph Valid Tree. Instead of asking
whether the whole graph forms one valid tree, we ask how many separate groups
exist after all edges are considered.

DFS/BFS would also work well by building an adjacency list and counting how
many searches we need to start. Union-Find is especially neat here because the
component count naturally falls by one whenever an edge connects two groups
that were not already connected.
"""

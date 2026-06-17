"""
Problem 1971: Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/

There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1. Given edges, source, and destination, return True if there is
a valid path from source to destination, otherwise return False.

Examples:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: True

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: False
"""

from collections import defaultdict, deque
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
    ) -> bool:
        """
        BFS over an adjacency list.

        Time Complexity: O(n + e) - Visit vertices and edges once.
        Space Complexity: O(n + e) - Adjacency list and visited set.
        """
        if source == destination:
            return True

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == destination:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False


if __name__ == "__main__":
    sol = Solution()

    test(
        sol.validPath,
        3,
        [[0, 1], [1, 2], [2, 0]],
        0,
        2,
        True,
        "Test 1 - Connected graph",
    )
    test(
        sol.validPath,
        6,
        [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
        0,
        5,
        False,
        "Test 2 - Disconnected graph",
    )
    test(sol.validPath, 1, [], 0, 0, True, "Test 3 - Source is destination")

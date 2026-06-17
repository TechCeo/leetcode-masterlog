"""
Problem 133: Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy
of the graph.

Each node contains a value and a list of its neighbors.

Examples:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
"""

from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        DFS with a hash map from original nodes to clone nodes.

        Time Complexity: O(v + e) - Visit each node and edge once.
        Space Complexity: O(v) - Store one clone per node.
        """
        old_to_new = {}

        def clone(current: Node) -> Node:
            if current in old_to_new:
                return old_to_new[current]

            copied = Node(current.val)
            old_to_new[current] = copied

            for neighbor in current.neighbors:
                copied.neighbors.append(clone(neighbor))

            return copied

        return clone(node) if node else None


def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[val - 1] for val in neighbors]

    return nodes[0]


def graph_to_adj_list(node):
    if not node:
        return []

    visited = {}
    stack = [node]

    while stack:
        current = stack.pop()
        if current.val in visited:
            continue

        visited[current.val] = current
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                stack.append(neighbor)

    return [
        sorted(neighbor.val for neighbor in visited[val].neighbors)
        for val in sorted(visited)
    ]


def shares_nodes(original, copied):
    if not original or not copied:
        return False

    original_nodes = set()
    stack = [original]

    while stack:
        current = stack.pop()
        if current in original_nodes:
            continue

        original_nodes.add(current)
        stack.extend(current.neighbors)

    stack = [copied]
    seen_copies = set()

    while stack:
        current = stack.pop()
        if current in seen_copies:
            continue

        if current in original_nodes:
            return True

        seen_copies.add(current)
        stack.extend(current.neighbors)

    return False


def test_clone_graph(adj_list, name):
    sol = Solution()
    original = build_graph(adj_list)
    copied = sol.cloneGraph(original)
    result = graph_to_adj_list(copied)

    if result == adj_list and not shares_nodes(original, copied):
        print(f"{name} Passed")
    else:
        print(f"{name} Failed")
        print(f"   Output:   {result}")
        print(f"   Expected: {adj_list}")


if __name__ == "__main__":
    test_clone_graph([[2, 4], [1, 3], [2, 4], [1, 3]], "Test 1 - Cycle graph")
    test_clone_graph([[]], "Test 2 - Single node")
    test_clone_graph([], "Test 3 - Empty graph")

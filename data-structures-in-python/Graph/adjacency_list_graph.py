"""
Graph (Adjacency List)
----------------------

A graph models relationships between vertices. An adjacency list stores each
vertex alongside its neighboring vertices, using O(V + E) space.

This implementation supports directed and undirected, unweighted graphs.
Breadth-first search (BFS) and depth-first search (DFS) both take O(V + E)
time over the reachable portion of the graph.

Common Uses:
- Networks and routes
- Dependency relationships
- Social connections
- Grid and state-space problems
"""

from collections import deque


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self._adjacency = {}

    def add_vertex(self, vertex) -> bool:
        if vertex in self._adjacency:
            return False
        self._adjacency[vertex] = []
        return True

    def add_edge(self, source, destination):
        """Add missing vertices automatically and avoid duplicate edges."""
        self.add_vertex(source)
        self.add_vertex(destination)

        if destination not in self._adjacency[source]:
            self._adjacency[source].append(destination)

        if not self.directed and source not in self._adjacency[destination]:
            self._adjacency[destination].append(source)

    def remove_edge(self, source, destination) -> bool:
        if source not in self._adjacency:
            return False

        removed = False
        if destination in self._adjacency[source]:
            self._adjacency[source].remove(destination)
            removed = True

        if (
            not self.directed
            and destination in self._adjacency
            and source in self._adjacency[destination]
        ):
            self._adjacency[destination].remove(source)

        return removed

    def remove_vertex(self, vertex) -> bool:
        if vertex not in self._adjacency:
            return False

        del self._adjacency[vertex]
        for neighbors in self._adjacency.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

        return True

    def neighbors(self, vertex) -> list:
        if vertex not in self._adjacency:
            raise KeyError(vertex)
        return self._adjacency[vertex].copy()

    def bfs(self, start) -> list:
        if start not in self._adjacency:
            raise KeyError(start)

        order = []
        visited = {start}
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in self._adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start) -> list:
        if start not in self._adjacency:
            raise KeyError(start)

        order = []
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue

            visited.add(vertex)
            order.append(vertex)

            # Reverse preserves the insertion order used by recursive DFS.
            for neighbor in reversed(self._adjacency[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return order

    def vertices(self) -> list:
        return list(self._adjacency)

    def __repr__(self) -> str:
        return f"Graph(directed={self.directed}, adjacency={self._adjacency})"


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_vertex("E")

    assert graph.neighbors("A") == ["B", "C"]
    assert graph.bfs("A") == ["A", "B", "C", "D"]
    assert graph.dfs("A") == ["A", "B", "D", "C"]
    assert graph.remove_edge("A", "C")
    assert "A" not in graph.neighbors("C")
    assert graph.remove_vertex("D")
    assert "D" not in graph.neighbors("B")

    directed_graph = Graph(directed=True)
    directed_graph.add_edge(1, 2)
    assert directed_graph.neighbors(1) == [2]
    assert directed_graph.neighbors(2) == []

    print("All adjacency_list_graph tests passed.")

"""
Disjoint Set (Union-Find)
-------------------------

A disjoint set tracks non-overlapping groups of elements. It quickly answers
whether two elements belong to the same connected component.

Path compression flattens trees during find operations, and union by size
attaches the smaller tree beneath the larger one. Together, they make each
operation effectively O(1) amortized: O(alpha(n)), where alpha grows extremely
slowly.

Common Uses:
- Detecting cycles in undirected graphs
- Kruskal's minimum spanning tree algorithm
- Dynamic connectivity problems
"""


class DisjointSet:
    def __init__(self, size: int):
        if size < 0:
            raise ValueError("Size cannot be negative.")

        self.parent = list(range(size))
        self.component_size = [1] * size
        self._components = size

    def find(self, item: int) -> int:
        self._validate(item)

        # Point every node on the path at its grandparent.
        while item != self.parent[item]:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]

        return item

    def union(self, first: int, second: int) -> bool:
        """Merge two components. Return False if already connected."""
        first_root = self.find(first)
        second_root = self.find(second)

        if first_root == second_root:
            return False

        if self.component_size[first_root] < self.component_size[second_root]:
            first_root, second_root = second_root, first_root

        self.parent[second_root] = first_root
        self.component_size[first_root] += self.component_size[second_root]
        self._components -= 1
        return True

    def connected(self, first: int, second: int) -> bool:
        return self.find(first) == self.find(second)

    def size_of(self, item: int) -> int:
        return self.component_size[self.find(item)]

    def component_count(self) -> int:
        return self._components

    def _validate(self, item: int):
        if item < 0 or item >= len(self.parent):
            raise IndexError("Disjoint set index out of range.")

    def __repr__(self) -> str:
        groups = {}
        for item in range(len(self.parent)):
            groups.setdefault(self.find(item), []).append(item)
        return f"DisjointSet({list(groups.values())})"


if __name__ == "__main__":
    disjoint_set = DisjointSet(7)
    assert disjoint_set.union(0, 1)
    assert disjoint_set.union(1, 2)
    assert disjoint_set.union(3, 4)
    assert not disjoint_set.union(0, 2)

    assert disjoint_set.connected(0, 2)
    assert not disjoint_set.connected(0, 3)
    assert disjoint_set.size_of(1) == 3
    assert disjoint_set.component_count() == 4

    disjoint_set.union(2, 4)
    assert disjoint_set.connected(0, 3)
    assert disjoint_set.size_of(4) == 5
    assert disjoint_set.component_count() == 3

    print("All union_find tests passed.")

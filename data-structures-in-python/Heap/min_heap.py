"""
Binary Min-Heap
---------------

A min-heap is a complete binary tree where every parent is less than or equal
to its children. The minimum value is always stored at the root.

The tree is represented by an array. For an item at index i:
- Parent: (i - 1) // 2
- Left child: 2 * i + 1
- Right child: 2 * i + 2

Common Uses:
- Priority queues
- Dijkstra's and Prim's algorithms
- Finding the smallest or largest k elements
"""


class MinHeap:
    def __init__(self, values=None):
        self._heap = list(values) if values is not None else []

        # Bottom-up heap construction takes O(n) time.
        for index in range(len(self._heap) // 2 - 1, -1, -1):
            self._sift_down(index)

    def is_empty(self) -> bool:
        return not self._heap

    def size(self) -> int:
        return len(self._heap)

    def peek(self):
        """Return the minimum value in O(1) time."""
        if self.is_empty():
            raise IndexError("Peek from an empty heap.")
        return self._heap[0]

    def push(self, value):
        """Add a value in O(log n) time."""
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        """Remove and return the minimum value in O(log n) time."""
        if self.is_empty():
            raise IndexError("Pop from an empty heap.")

        self._swap(0, len(self._heap) - 1)
        minimum = self._heap.pop()

        if self._heap:
            self._sift_down(0)

        return minimum

    def _sift_up(self, index: int):
        while index > 0:
            parent = (index - 1) // 2
            if self._heap[parent] <= self._heap[index]:
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index: int):
        size = len(self._heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < size and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == index:
                return

            self._swap(index, smallest)
            index = smallest

    def _swap(self, first: int, second: int):
        self._heap[first], self._heap[second] = (
            self._heap[second],
            self._heap[first],
        )

    def to_list(self) -> list:
        """Return the internal level-order representation."""
        return self._heap.copy()

    def __repr__(self) -> str:
        return f"MinHeap({self._heap})"


if __name__ == "__main__":
    heap = MinHeap([9, 4, 7, 1, 3, 6])
    assert heap.peek() == 1

    heap.push(2)
    assert heap.peek() == 1
    assert [heap.pop() for _ in range(heap.size())] == [1, 2, 3, 4, 6, 7, 9]
    assert heap.is_empty()

    try:
        heap.pop()
        raise AssertionError("An empty heap should raise IndexError.")
    except IndexError:
        pass

    print("All min_heap tests passed.")

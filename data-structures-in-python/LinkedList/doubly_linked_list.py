"""
Doubly Linked List
------------------

Each node stores links to both its next and previous neighbors. This costs an
extra pointer per node but supports movement in either direction and O(1)
removal when a node is already known.

Common Uses:
- Browser back/forward navigation
- LRU caches
- Deques and ordered collections
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node

        self.head = new_node
        self._size += 1

    def append(self, value):
        new_node = Node(value)
        new_node.previous = self.tail

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def insert(self, index: int, value):
        if index < 0 or index > self._size:
            raise IndexError("Linked list index out of range.")
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return

        current = self._node_at(index)
        new_node = Node(value)
        previous = current.previous

        new_node.previous = previous
        new_node.next = current
        previous.next = new_node
        current.previous = new_node
        self._size += 1

    def remove(self, value) -> bool:
        current = self.head

        while current:
            if current.value == value:
                self._unlink(current)
                return True
            current = current.next

        return False

    def get(self, index: int):
        return self._node_at(index).value

    def to_list(self) -> list:
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def to_reversed_list(self) -> list:
        values = []
        current = self.tail

        while current:
            values.append(current.value)
            current = current.previous

        return values

    def _unlink(self, node: Node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        self._size -= 1

    def _node_at(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError("Linked list index out of range.")

        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - index - 1):
                current = current.previous

        return current

    def __repr__(self) -> str:
        return f"DoublyLinkedList({self.to_list()})"


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append("b")
    linked_list.prepend("a")
    linked_list.append("d")
    linked_list.insert(2, "c")

    assert linked_list.to_list() == ["a", "b", "c", "d"]
    assert linked_list.to_reversed_list() == ["d", "c", "b", "a"]
    assert linked_list.get(2) == "c"
    assert linked_list.remove("a")
    assert linked_list.remove("d")
    assert linked_list.to_list() == ["b", "c"]
    assert linked_list.head.previous is None
    assert linked_list.tail.next is None
    assert linked_list.size() == 2

    print("All doubly_linked_list tests passed.")

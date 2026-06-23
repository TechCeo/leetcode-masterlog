"""
Singly Linked List
------------------

A linked list stores values in nodes. Each node points to the next node, so
the structure can grow without shifting existing elements.

Common Uses:
- Implementing stacks and queues
- Frequent insertion or deletion at the front
- Representing chains such as graph adjacency lists

Trade-off:
Prepending is O(1), but accessing an item by position is O(n).
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def prepend(self, value):
        """Add a value to the front in O(1) time."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def append(self, value):
        """Add a value to the end in O(1) time."""
        new_node = Node(value)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def insert(self, index: int, value):
        """Insert before index. Allow index == size to append."""
        if index < 0 or index > self._size:
            raise IndexError("Linked list index out of range.")
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return

        previous = self._node_at(index - 1)
        new_node = Node(value)
        new_node.next = previous.next
        previous.next = new_node
        self._size += 1

    def remove(self, value) -> bool:
        """Remove the first matching value and report whether it was found."""
        previous = None
        current = self.head

        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current is self.tail:
                    self.tail = previous

                self._size -= 1
                return True

            previous = current
            current = current.next

        return False

    def get(self, index: int):
        return self._node_at(index).value

    def find(self, value) -> int:
        """Return the first matching index, or -1 when absent."""
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def to_list(self) -> list:
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def _node_at(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError("Linked list index out of range.")

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.to_list()})"


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    assert linked_list.is_empty()

    linked_list.append(20)
    linked_list.prepend(10)
    linked_list.append(40)
    linked_list.insert(2, 30)

    assert linked_list.to_list() == [10, 20, 30, 40]
    assert linked_list.get(2) == 30
    assert linked_list.find(40) == 3
    assert linked_list.remove(10)
    assert linked_list.remove(40)
    assert not linked_list.remove(99)
    assert linked_list.to_list() == [20, 30]
    assert linked_list.head.value == 20
    assert linked_list.tail.value == 30
    assert linked_list.size() == 2

    print("All singly_linked_list tests passed.")

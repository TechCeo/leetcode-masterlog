"""
Stack (Linked List Implementation)
----------------------------------

A stack is a linear data structure that follows the Last In First Out (LIFO) principle — 
the last element added is the first one to be removed. Think of it like a stack of plates:
you add to the top and remove from the top.

This implementation uses a singly linked list to support dynamic memory allocation — 
meaning the stack can grow or shrink as needed without resizing an underlying array.

Key Operations:
- push(x): Add element x to the top of the stack.
- pop(): Remove and return the top element.
- peek(): Return the top element without removing it.
- is_empty(): Check whether the stack is empty.
- size(): Return the number of elements in the stack.

Use Cases:
- Undo functionality in editors and IDEs
- Parsing expressions and syntax (e.g., matching parentheses)
- Backtracking algorithms (e.g., DFS in graphs or mazes)
- Function call management in recursion (call stack)

Why Use a Linked List?
- Unlike array-based stacks, linked lists don’t require resizing or pre-allocation.
- Each push/pop is O(1) without memory shifts.
- Especially useful when stack size is highly variable or unknown in advance.
"""


# stack_linkedlist.py

class Node:
    """Node for singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """Stack implementation using singly linked list (LIFO)."""
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item):
        """Push an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top item. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")

        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.value

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.top.value

    def size(self) -> int:
        """Return the number of items in the stack."""
        return self._size

    def __repr__(self):
        items = []
        current = self.top
        while current:
            items.append(current.value)
            current = current.next
        return f"Stack(top → bottom): {items}"


# Example usage and test cases
if __name__ == "__main__":
    stack = Stack()
    print("Is empty?", stack.is_empty())  # True

    stack.push(5)
    stack.push(10)
    stack.push(15)
    print("Stack after pushes:", stack)  # Stack(top → bottom): [15, 10, 5]

    print("Peek:", stack.peek())         # 15
    print("Pop:", stack.pop())           # 15
    print("Stack after pop:", stack)     # Stack(top → bottom): [10, 5]
    print("Size:", stack.size())         # 2

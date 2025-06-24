"""
Stack (Array-Based Implementation)
----------------------------------

A stack is a Last In First Out (LIFO) data structure — the most recently added item is the first to be removed.

This version uses a dynamic array (Python list) for internal storage, offering efficient O(1) time complexity for push and pop operations (on average).

Common Uses:
- Undo functionality
- Expression evaluation and parsing
- Function call stacks
- Navigation history in browsers

Note:
While simple and fast, array-based stacks may require resizing operations under the hood as they grow.
"""


class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.items[-1]

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

    def __repr__(self):
        return f"Stack({self.items})"


# Example usage and simple test cases
if __name__ == "__main__":
    stack = Stack()
    print("Is empty?", stack.is_empty())  # True

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack)  # Stack([10, 20, 30])

    print("Peek:", stack.peek())         # 30
    print("Pop:", stack.pop())           # 30
    print("Stack after pop:", stack)     # Stack([10, 20])
    print("Size:", stack.size())         # 2

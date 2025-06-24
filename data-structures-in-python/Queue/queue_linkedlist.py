"""
Queue (Linked List–based)

A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
This version uses a linked list to efficiently support O(1) enqueue and dequeue operations.

Use Cases:
- Task scheduling (CPU scheduling, print queues)
- Breadth-first search (BFS) in graphs
- Real-time systems (message queues, buffers)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node

        if not self.front:
            self.front = new_node

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        dequeued_value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None

        self._size -= 1
        return dequeued_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size


# --- Tests ---
if __name__ == "__main__":
    q = LinkedListQueue()
    assert q.is_empty() == True, "Test 1 Failed: Queue should be empty"

    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)

    assert q.peek() == 100, "Test 2 Failed: Front of queue should be 100"
    assert q.dequeue() == 100, "Test 3 Failed: Dequeued value should be 100"
    assert q.dequeue() == 200, "Test 4 Failed: Dequeued value should be 200"
    assert q.size() == 1, "Test 5 Failed: Queue size should be 1"
    assert q.is_empty() == False, "Test 6 Failed: Queue should not be empty"

    q.dequeue()
    assert q.is_empty() == True, "Test 7 Failed: Queue should be empty again"

    print(" All linked list–based queue tests passed.")

"""
Queue (Array-based)

A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue).

Use Cases:
- Task scheduling (CPU scheduling, print queues)
- Breadth-first search (BFS) in graphs
- Real-time systems (message queues, buffers)
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# --- Tests ---
if __name__ == "__main__":
    q = Queue()
    assert q.is_empty() == True, "Test 1 Failed: Queue should be empty"
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    assert q.peek() == 10, "Test 2 Failed: Front of queue should be 10"
    assert q.dequeue() == 10, "Test 3 Failed: Dequeued value should be 10"
    assert q.dequeue() == 20, "Test 4 Failed: Dequeued value should be 20"
    assert q.size() == 1, "Test 5 Failed: Queue size should be 1"
    assert q.is_empty() == False, "Test 6 Failed: Queue should not be empty"
    
    q.dequeue()
    assert q.is_empty() == True, "Test 7 Failed: Queue should be empty again"
    
    print("All queue_array tests passed.")

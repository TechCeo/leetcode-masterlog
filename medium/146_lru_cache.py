"""
Problem 146: LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that simulates a Least Recently Used (LRU) cache.

Implement:
- get(key): return the value if present, else -1
- put(key, value): update or insert key-value pair, evict LRU if over capacity

Both operations must run in O(1) time.

Examples:
Input: ["LRUCache", [2], "put", [1, 10], "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
Output: [None, None, 10, None, None, 20, -1]

Constraints:
- 1 <= capacity <= 100
- 0 <= key, value <= 1000
"""

class Dlinked:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.container = {}

        # dummy left (LRU) and right (MRU) pointers
        self.left = Dlinked(0, 0)
        self.right = Dlinked(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Dlinked):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Dlinked):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.container:
            node = self.container[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.container:
            self.remove(self.container[key])
        self.container[key] = Dlinked(key, value)
        self.insert(self.container[key])

        if len(self.container) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.container[lru.key]

if __name__ == "__main__":
    print("LRU Cache Test:")
    lru = LRUCache(2)
    lru.put(1, 10)  # cache: {1=10}
    print("put(1, 10)")
    print("get(1) →", lru.get(1))  # should return 10

    lru.put(2, 20)  # cache: {1=10, 2=20}
    print("put(2, 20)")

    lru.put(3, 30)  # evicts key 1 → cache: {2=20, 3=30}
    print("put(3, 30)")

    print("get(2) →", lru.get(2))  # should return 20
    print("get(1) →", lru.get(1))  # should return -1 (evicted)

"""
Reflection:
This was one of my favorite problems to solve — not just because it involved a clean use of OOP and reasoning,
but because it modeled something real. I enjoyed building a system that mirrors a real-world cache mechanism.
It was a rewarding experience to combine a hashmap and a doubly linked list for constant time operations — a common pattern in system design.
"""

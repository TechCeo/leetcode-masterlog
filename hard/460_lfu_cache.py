"""
460. LFU Cache
https://leetcode.com/problems/lfu-cache/

Design a Least Frequently Used cache whose get and put operations run in
average O(1) time. When frequencies tie, evict the least recently used key.
"""

from collections import defaultdict
from typing import Dict, List, Optional, Tuple
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class DoublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def append(self, node: Node) -> None:
        previous = self.right.prev
        previous.next = node
        node.prev = previous
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def pop_lru(self) -> Node:
        node = self.left.next
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minimum_frequency = 0
        self.nodes: Dict[int, Node] = {}
        self.frequency_lists = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._increase_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._increase_frequency(node)
            return

        if self.size == self.capacity:
            lru = self.frequency_lists[self.minimum_frequency].pop_lru()
            del self.nodes[lru.key]
            self.size -= 1

        node = Node(key, value)
        self.nodes[key] = node
        self.frequency_lists[1].append(node)
        self.minimum_frequency = 1
        self.size += 1

    def _increase_frequency(self, node: Node) -> None:
        old_frequency = node.frequency
        old_list = self.frequency_lists[old_frequency]
        old_list.remove(node)

        if old_frequency == self.minimum_frequency and old_list.size == 0:
            self.minimum_frequency += 1

        node.frequency += 1
        self.frequency_lists[node.frequency].append(node)


def run_operations(
    capacity: int,
    operations: List[Tuple],
) -> List[Optional[int]]:
    cache = LFUCache(capacity)
    output = []

    for operation in operations:
        if operation[0] == "put":
            cache.put(operation[1], operation[2])
            output.append(None)
        else:
            output.append(cache.get(operation[1]))

    return output


if __name__ == "__main__":
    test(
        run_operations,
        2,
        [
            ("put", 1, 1),
            ("put", 2, 2),
            ("get", 1),
            ("put", 3, 3),
            ("get", 2),
            ("get", 3),
            ("put", 4, 4),
            ("get", 1),
            ("get", 3),
            ("get", 4),
        ],
        [None, None, 1, None, -1, 3, None, -1, 3, 4],
        "Test 1 - Frequency and recency eviction",
    )
    test(
        run_operations,
        0,
        [("put", 1, 1), ("get", 1)],
        [None, -1],
        "Test 2 - Zero capacity",
    )
    test(
        run_operations,
        2,
        [("put", 1, 1), ("put", 1, 10), ("get", 1)],
        [None, None, 10],
        "Test 3 - Update existing key",
    )


"""
Reflection:
A hash map finds each key in O(1), while one doubly linked list per frequency
tracks recency among keys with the same usage count.

The minimum frequency identifies the eviction bucket immediately. Inside that
bucket, the node nearest the left sentinel is the least recently used one.
"""

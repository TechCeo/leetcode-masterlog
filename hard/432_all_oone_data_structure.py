"""
432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/

Design a data structure that increments and decrements string counts and
returns a key with the maximum or minimum count. Every operation must run in
average O(1) time.
"""

from typing import Dict, List, Optional, Set, Tuple
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.test_utils import test


class Bucket:
    def __init__(self, count: int):
        self.count = count
        self.keys: Set[str] = set()
        self.prev: Optional['Bucket'] = None
        self.next: Optional['Bucket'] = None


class AllOne:
    def __init__(self):
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_buckets: Dict[str, Bucket] = {}

    def inc(self, key: str) -> None:
        if key not in self.key_buckets:
            first = self.head.next
            if first is self.tail or first.count != 1:
                first = self._insert_after(self.head, Bucket(1))
            first.keys.add(key)
            self.key_buckets[key] = first
            return

        current = self.key_buckets[key]
        target = current.next

        if target is self.tail or target.count != current.count + 1:
            target = self._insert_after(current, Bucket(current.count + 1))

        self._move_key(key, current, target)

    def dec(self, key: str) -> None:
        current = self.key_buckets[key]

        if current.count == 1:
            current.keys.remove(key)
            del self.key_buckets[key]
            self._remove_if_empty(current)
            return

        target = current.prev
        if target is self.head or target.count != current.count - 1:
            target = self._insert_after(current.prev, Bucket(current.count - 1))

        self._move_key(key, current, target)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _move_key(self, key: str, source: Bucket, target: Bucket) -> None:
        source.keys.remove(key)
        target.keys.add(key)
        self.key_buckets[key] = target
        self._remove_if_empty(source)

    def _insert_after(self, bucket: Bucket, new_bucket: Bucket) -> Bucket:
        next_bucket = bucket.next
        bucket.next = new_bucket
        new_bucket.prev = bucket
        new_bucket.next = next_bucket
        next_bucket.prev = new_bucket
        return new_bucket

    def _remove_if_empty(self, bucket: Bucket) -> None:
        if bucket.keys:
            return
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev


def run_operations(operations: List[Tuple[str, ...]]) -> List[str]:
    structure = AllOne()
    output = []

    for operation in operations:
        name = operation[0]
        if name == "inc":
            structure.inc(operation[1])
        elif name == "dec":
            structure.dec(operation[1])
        elif name == "max":
            output.append(structure.getMaxKey())
        else:
            output.append(structure.getMinKey())

    return output


if __name__ == "__main__":
    test(
        run_operations,
        [
            ("inc", "hello"),
            ("inc", "hello"),
            ("inc", "leet"),
            ("max",),
            ("min",),
        ],
        ["hello", "leet"],
        "Test 1 - Maximum and minimum keys",
    )
    test(
        run_operations,
        [
            ("inc", "a"),
            ("inc", "b"),
            ("inc", "b"),
            ("dec", "b"),
            ("dec", "a"),
            ("max",),
            ("min",),
            ("dec", "b"),
            ("max",),
            ("min",),
        ],
        ["b", "b", "", ""],
        "Test 2 - Decrement and remove keys",
    )
    test(
        run_operations,
        [("max",), ("min",)],
        ["", ""],
        "Test 3 - Empty structure",
    )


"""
Reflection:
The linked list stores count buckets in increasing order, and each bucket holds
all keys with that count. A hash map points each key directly to its bucket.

Incrementing or decrementing moves a key only one bucket away. Empty buckets
are removed immediately, so the first and last buckets always hold the minimum
and maximum counts.
"""

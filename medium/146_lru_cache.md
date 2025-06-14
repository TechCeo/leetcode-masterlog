# 146. LRU Cache

🔗 https://leetcode.com/problems/lru-cache/

---

## Problem Summary

Design a data structure that implements an LRU (Least Recently Used) cache with fixed capacity. The cache must support:
- `get(key)`: return the value if it exists, else -1
- `put(key, value)`: update the value or insert the key. If the cache exceeds capacity, evict the least recently used key.

Both operations must run in O(1) average time.

---

## Reflection

This was one of my favorite LeetCode problems — not just because of the clever use of data structures, but because it models a real-world system. Building this cache wasn't about brute-forcing a solution; it required a deep understanding of object-oriented design, memory-efficient data structures, and algorithmic guarantees.

The combination of a hashmap and a doubly linked list unlocked constant time lookups and insertions while maintaining the least-recently-used ordering. It felt like solving a miniature system design challenge — I had to design and build an internal memory manager, enforce ordering rules, and handle edge cases like eviction and reordering.

What I particularly enjoyed was how this problem bridged low-level pointer manipulation with high-level behavior — the same pattern used in real systems like CPU memory caches, database page replacements, and web content caching.

This problem was also a perfect exercise in clean, extensible OOP: I built a custom `Dlinked` class for the doubly linked list nodes, and managed `left` and `right` dummy pointers to avoid special cases when updating the list ends.

---

## Caches in Real-World Software

Caches play a critical role in software performance and scalability. They're everywhere:
- Web browsers cache pages and assets to speed up page loads
- Databases cache query results or table pages to reduce disk reads
- Operating systems cache memory pages for fast access
- Distributed systems use caching layers (e.g., Redis) to offload expensive computations

Understanding how LRU caches work isn’t just useful for coding interviews — it’s foundational knowledge for any engineer building high-performance systems.

---

## Complexity

- Time: O(1) for both get and put operations
- Space: O(n) for storing up to `capacity` key-value pairs + linked list nodes

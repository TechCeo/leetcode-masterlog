"""
Hash Table (Separate Chaining)
------------------------------

A hash table maps keys to values by converting each key into a bucket index.
Collisions are handled by storing multiple key-value pairs in the same bucket.

Average Complexity:
- Set, get, remove: O(1)
- Space: O(n)

The table resizes when its load factor exceeds 0.75. Worst-case operations are
O(n) when many keys collide.
"""


class HashTable:
    def __init__(self, capacity: int = 8):
        if capacity < 1:
            raise ValueError("Capacity must be positive.")

        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def set(self, key, value):
        bucket = self._bucket(key)

        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self._size / len(self._buckets) > 0.75:
            self._resize(len(self._buckets) * 2)

    def get(self, key):
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value
        raise KeyError(key)

    def remove(self, key):
        bucket = self._bucket(key)

        for index, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                self._size -= 1
                return value

        raise KeyError(key)

    def contains(self, key) -> bool:
        return any(stored_key == key for stored_key, _ in self._bucket(key))

    def keys(self) -> list:
        return [key for bucket in self._buckets for key, _ in bucket]

    def _bucket(self, key) -> list:
        return self._buckets[hash(key) % len(self._buckets)]

    def _resize(self, new_capacity: int):
        old_items = [item for bucket in self._buckets for item in bucket]
        self._buckets = [[] for _ in range(new_capacity)]

        for key, value in old_items:
            self._bucket(key).append((key, value))

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key) -> bool:
        return self.contains(key)

    def __repr__(self) -> str:
        items = {key: value for bucket in self._buckets for key, value in bucket}
        return f"HashTable({items})"


if __name__ == "__main__":
    table = HashTable(capacity=2)
    assert table.is_empty()

    table.set("name", "Ada")
    table.set("language", "Python")
    table.set("year", 1991)
    table.set("year", 1990)

    assert table.get("name") == "Ada"
    assert table.get("year") == 1990
    assert "language" in table
    assert table.remove("language") == "Python"
    assert "language" not in table
    assert len(table) == 2

    try:
        table.get("missing")
        raise AssertionError("Missing keys should raise KeyError.")
    except KeyError:
        pass

    print("All hash_table tests passed.")

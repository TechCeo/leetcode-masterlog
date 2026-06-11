"""
Problem 981: Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values
for the same key at different timestamps and retrieve the key's value at a
certain timestamp.

Implement:
- set(key, value, timestamp): stores the key with the given value at timestamp.
- get(key, timestamp): returns the value with the largest timestamp <= timestamp.
  If there is no such value, return "".

Examples:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[None, None, "bar", "bar", None, "bar2", "bar2"]

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits
- 1 <= timestamp <= 10^7
- All timestamps of set are strictly increasing for each key
"""

from collections import defaultdict
from typing import List, Tuple


class TimeMap:
    def __init__(self):
        self.store: dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store each key's history in timestamp order.

        Time Complexity: O(1)
        Space Complexity: O(n) - Total number of set calls.
        """
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Binary search for the rightmost timestamp <= requested timestamp.

        Time Complexity: O(log n) - n is the number of values for this key.
        Space Complexity: O(1)
        """
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            saved_timestamp, saved_value = values[mid]

            if saved_timestamp <= timestamp:
                result = saved_value
                left = mid + 1
            else:
                right = mid - 1

        return result


def run_time_map_test(operations: List[str], inputs: List[List], expected: List, name: str) -> None:
    time_map = None
    result = []

    for operation, args in zip(operations, inputs):
        if operation == "TimeMap":
            time_map = TimeMap()
            result.append(None)
        elif operation == "set":
            time_map.set(*args)
            result.append(None)
        elif operation == "get":
            result.append(time_map.get(*args))

    if result == expected:
        print(f"{name} Passed")
    else:
        print(f"{name} Failed")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}")


if __name__ == "__main__":
    run_time_map_test(
        ["TimeMap", "set", "get", "get", "set", "get", "get"],
        [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
        [None, None, "bar", "bar", None, "bar2", "bar2"],
        "Test 1 - Basic timestamp lookup",
    )

    run_time_map_test(
        ["TimeMap", "set", "set", "get", "get", "get"],
        [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15]],
        [None, None, None, "", "high", "high"],
        "Test 2 - Before and between timestamps",
    )

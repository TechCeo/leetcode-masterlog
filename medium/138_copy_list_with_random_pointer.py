"""
Problem 138: Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list or null.

Construct a deep copy of the list. The copied list should consist of exactly
n brand-new nodes, where each new node has the same value and random pointer
relationships as the original list.

Examples:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Hash map approach.

        First pass:
        - Create a clone node for every original node.

        Second pass:
        - Wire each clone's next and random pointers using the map.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        old_to_copy = {None: None}
        current = head

        while current:
            old_to_copy[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = old_to_copy[current]
            copy.next = old_to_copy[current.next]
            copy.random = old_to_copy[current.random]
            current = current.next

        return old_to_copy[head]


def build_random_list(values):
    if not values:
        return None

    nodes = [Node(value) for value, _ in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, random_index) in enumerate(values):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def random_list_to_array(head):
    nodes = []
    index_by_node = {}
    current = head

    while current:
        index_by_node[current] = len(nodes)
        nodes.append(current)
        current = current.next

    result = []
    for node in nodes:
        random_index = index_by_node[node.random] if node.random else None
        result.append([node.val, random_index])

    return result


def shares_nodes(original, copied):
    seen = set()

    while original:
        seen.add(original)
        original = original.next

    while copied:
        if copied in seen:
            return True
        copied = copied.next

    return False


def test_random_copy(values, name):
    sol = Solution()
    original = build_random_list(values)
    copied = sol.copyRandomList(original)

    result = random_list_to_array(copied)
    expected = [[value, random_index] for value, random_index in values]

    if result == expected and not shares_nodes(original, copied):
        print(f"{name} Passed")
    else:
        print(f"{name} Failed")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}")


if __name__ == "__main__":
    test_random_copy(
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        "Test 1 - Mixed random pointers",
    )
    test_random_copy([[1, 1], [2, 1]], "Test 2 - Self random pointer")
    test_random_copy([], "Test 3 - Empty list")

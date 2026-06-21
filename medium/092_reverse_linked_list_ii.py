"""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right, reverse
the nodes from position left to position right and return the modified list.

Example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""

from typing import Optional
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test_ll


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        """
        Reverse the requested section in place using front insertion.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        before = dummy

        for _ in range(left - 1):
            before = before.next

        current = before.next

        for _ in range(right - left):
            moving = current.next
            current.next = moving.next
            moving.next = before.next
            before.next = moving

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    test_ll(
        sol.reverseBetween,
        build_linked_list([1, 2, 3, 4, 5]),
        2,
        4,
        [1, 4, 3, 2, 5],
        "Test 1 - Reverse middle section",
    )
    test_ll(
        sol.reverseBetween,
        build_linked_list([5]),
        1,
        1,
        [5],
        "Test 2 - Single node",
    )
    test_ll(
        sol.reverseBetween,
        build_linked_list([1, 2, 3]),
        1,
        3,
        [3, 2, 1],
        "Test 3 - Reverse entire list",
    )
    test_ll(
        sol.reverseBetween,
        build_linked_list([1, 2, 3, 4]),
        3,
        4,
        [1, 2, 4, 3],
        "Test 4 - Reverse through tail",
    )


"""
Reflection:
The dummy node removes the special case where the reversal starts at the head.

The node at the start of the section stays fixed while each following node is
moved to the front of the section. This reverses only the requested range and
keeps every connection outside that range intact.
"""

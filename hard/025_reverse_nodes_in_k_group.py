"""
Problem 25: Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k, the remaining nodes at
the end should stay in their original order.

Examples:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test_ll


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Iterative in-place reversal.

        For each complete group of k nodes:
        - Find the kth node.
        - Reverse the group.
        - Reconnect it to the previous and next groups.

        Time Complexity: O(n) - Each node is visited a constant number of times.
        Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev = group_next
            current = group_prev.next

            while current is not group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start

        return dummy.next

    def get_kth(self, current: ListNode, k: int) -> Optional[ListNode]:
        while current and k > 0:
            current = current.next
            k -= 1

        return current


if __name__ == "__main__":
    sol = Solution()

    test_ll(
        sol.reverseKGroup,
        build_linked_list([1, 2, 3, 4, 5]),
        2,
        [2, 1, 4, 3, 5],
        "Test 1 - Groups of two",
    )
    test_ll(
        sol.reverseKGroup,
        build_linked_list([1, 2, 3, 4, 5]),
        3,
        [3, 2, 1, 4, 5],
        "Test 2 - Remainder stays",
    )
    test_ll(
        sol.reverseKGroup,
        build_linked_list([1, 2, 3, 4]),
        4,
        [4, 3, 2, 1],
        "Test 3 - Whole list",
    )
    test_ll(
        sol.reverseKGroup,
        build_linked_list([1, 2, 3]),
        1,
        [1, 2, 3],
        "Test 4 - k is one",
    )

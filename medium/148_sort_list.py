"""
148. Sort List
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending
order.

Example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

from typing import Optional, Tuple
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test_ll


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Bottom-up merge sort.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        dummy = ListNode(0, head)
        run_size = 1

        while run_size < length:
            previous_tail = dummy
            current = dummy.next

            while current:
                left = current
                right = self._split(left, run_size)
                current = self._split(right, run_size)

                merged_head, merged_tail = self._merge(left, right)
                previous_tail.next = merged_head
                previous_tail = merged_tail

            run_size *= 2

        return dummy.next

    def _split(
        self,
        head: Optional[ListNode],
        size: int,
    ) -> Optional[ListNode]:
        if not head:
            return None

        for _ in range(size - 1):
            if not head.next:
                break
            head = head.next

        next_run = head.next
        head.next = None
        return next_run

    def _merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode],
    ) -> Tuple[ListNode, ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        while tail.next:
            tail = tail.next

        return dummy.next, tail


if __name__ == "__main__":
    sol = Solution()

    test_ll(
        sol.sortList,
        build_linked_list([4, 2, 1, 3]),
        [1, 2, 3, 4],
        "Test 1 - Unsorted list",
    )
    test_ll(
        sol.sortList,
        build_linked_list([-1, 5, 3, 4, 0]),
        [-1, 0, 3, 4, 5],
        "Test 2 - Negative values",
    )
    test_ll(
        sol.sortList,
        build_linked_list([3, 3, 1, 2, 1]),
        [1, 1, 2, 3, 3],
        "Test 3 - Duplicate values",
    )
    test_ll(sol.sortList, build_linked_list([]), [], "Test 4 - Empty list")


"""
Reflection:
Merge sort fits linked lists because merging only changes next pointers.

The bottom-up version begins with sorted runs of length one, then repeatedly
merges runs of size 1, 2, 4, and so on. It avoids recursion, which keeps the
extra space constant while preserving O(n log n) time.
"""

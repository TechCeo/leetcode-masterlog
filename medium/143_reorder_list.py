"""
143. Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from typing import Optional
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test_ll

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Three-step Process:
        1. Find Middle (Slow/Fast Pointers)
        2. Reverse Second Half (Iterative Reverse)
        3. Merge Halves (Alternating Splicing)
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        prev = slow.next = None  # Sever the first half from the second
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 3. Merge the two halves
        first, second = head, prev # 'prev' is now the head of the reversed second half
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

if __name__ == "__main__":
    sol = Solution()

    def test_wrapper(h):
        sol.reorderList(h)
        return h

    test_ll(test_wrapper, build_linked_list([1, 2, 3, 4]), [1, 4, 2, 3], "Even Length")
    test_ll(test_wrapper, build_linked_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3], "Odd Length")
    test_ll(test_wrapper, build_linked_list([1]), [1], "Single Node")
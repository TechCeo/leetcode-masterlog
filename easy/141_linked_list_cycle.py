"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

from typing import Optional
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Tortoise and Hare (Two Pointers)
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True

        return False



def setup_cycle(values, pos):
    """Helper to create a cycle for testing."""
    if pos == -1:
        return build_linked_list(values)
    
    head = build_linked_list(values)
    cycle_node = None
    curr = head
    tail = None
    
    idx = 0
    while curr:
        if idx == pos:
            cycle_node = curr
        if not curr.next:
            tail = curr
        curr = curr.next
        idx += 1
    
    if tail and cycle_node:
        tail.next = cycle_node
    return head

if __name__ == "__main__":
    sol = Solution()

    # Case 1: Cycle at index 1
    head1 = setup_cycle([3, 2, 0, -4], 1)
    test(sol.hasCycle, head1, True, "Cycle exists")

    # Case 2: Cycle at index 0
    head2 = setup_cycle([1, 2], 0)
    test(sol.hasCycle, head2, True, "Small cycle")

    # Case 3: No cycle
    head3 = setup_cycle([1], -1)
    test(sol.hasCycle, head3, False, "No cycle")
    
    
"""
Pattern: Fast and Slow Pointers
This is a core Linked List pattern. Beyond cycle detection, it is used for:

Finding the middle of a linked list: When fast reaches the end, slow is at the midpoint.
Finding the start of a cycle: Once they meet, moving one pointer to the head and moving both at speed 1 will cause them to meet again at the cycle's entry point.

"""

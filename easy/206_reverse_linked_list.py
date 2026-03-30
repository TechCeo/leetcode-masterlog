"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional
import sys, os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list, linked_list_to_list
# from utils.test_utils import test
from utils.test_utils import test_ll

    

class IterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            next_temp = curr.next 
            curr.next = prev      
            prev = curr           
            curr = next_temp
        
        return prev

class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n) - due to recursion stack
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursive step
        new_head = self.reverseList(head.next)
        
        # Reverse the current link
        # If A -> B, make B -> A
        head.next.next = head
        head.next = None
        
        return new_head

if __name__ == "__main__":
    iter_sol = IterativeSolution()
    rec_sol = RecursiveSolution()

    print("--- Testing Iterative ---")
    test_ll(iter_sol.reverseList, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Example 1")
    test_ll(iter_sol.reverseList, [1, 2], [2, 1], "Example 2")
    test_ll(iter_sol.reverseList, [], [], "Empty List")

    print("\n--- Testing Recursive ---")
    test_ll(rec_sol.reverseList, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Example 1")
    test_ll(rec_sol.reverseList, [], [], "Empty List")
"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
"""

from typing import Optional
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode
from utils.test_utils import test_ll

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach using a Dummy Node.
        
        Time Complexity: O(n + m) - Where n and m are lengths of the lists.
        Space Complexity: O(1) - We are rearranging existing nodes, not creating new ones.
        """
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining part of whichever list is not empty
        tail.next = list1 if list1 else list2

        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    
    # Import the builder for the test cases
    from utils.linked_list_utils import build_linked_list

    # Now we pass the built ListNodes to the test helper
    test_ll(
        sol.mergeTwoLists, 
        build_linked_list([1, 2, 4]), 
        build_linked_list([1, 3, 4]), 
        [1, 1, 2, 3, 4, 4], 
        "Standard Merge"
    )
    
    test_ll(
        sol.mergeTwoLists, 
        None, 
        None, 
        [], 
        "Both Empty"
    )
    
    test_ll(
        sol.mergeTwoLists, 
        None, 
        build_linked_list([0]), 
        [0], 
        "One Empty"
    )
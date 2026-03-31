"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list and an integer n, remove the nth node from the 
end of the list and return its head.
"""

from typing import Optional
import sys, os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode
from utils.test_utils import test_ll
from utils.linked_list_utils import build_linked_list, linked_list_to_list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two-pointer (Fast/Slow) approach with a Dummy Node.
        
        Time Complexity: O(sz) - Single pass through the list.
        Space Complexity: O(1) - Constant extra space used for pointers.
        """
        
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 1. Advance right pointer so it's n nodes ahead of left
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 2. Move both until right reaches the end
        # Left will stop exactly BEFORE the node to be deleted
        while right:
            left = left.next
            right = right.next
            
        # 3. Delete the nth node
        left.next = left.next.next

        
        return dummy.next

if __name__ == "__main__":
    sol = Solution()

    test_ll(sol.removeNthFromEnd, build_linked_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5], "Remove 2nd from end")
    test_ll(sol.removeNthFromEnd, build_linked_list([1]), 1, [], "Remove only node")
    test_ll(sol.removeNthFromEnd, build_linked_list([1, 2]), 2, [2], "Remove head node")
    test_ll(sol.removeNthFromEnd, build_linked_list([1, 2]), 1, [1], "Remove tail node")
"""
Problem 2: Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

Examples:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list
from utils.test_utils import test_ll


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Digit-by-digit addition with carry.

        Time Complexity: O(max(n, m)) - Visit each node from both lists once.
        Space Complexity: O(max(n, m)) - The output list stores the sum.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    test_ll(
        sol.addTwoNumbers,
        build_linked_list([2, 4, 3]),
        build_linked_list([5, 6, 4]),
        [7, 0, 8],
        "Test 1 - Same length",
    )
    test_ll(
        sol.addTwoNumbers,
        build_linked_list([0]),
        build_linked_list([0]),
        [0],
        "Test 2 - Zero",
    )
    test_ll(
        sol.addTwoNumbers,
        build_linked_list([9, 9, 9, 9, 9, 9, 9]),
        build_linked_list([9, 9, 9, 9]),
        [8, 9, 9, 9, 0, 0, 0, 1],
        "Test 3 - Carry across longer list",
    )

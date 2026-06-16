"""
Problem 23: Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked lists, each sorted in ascending order.
Merge all the linked lists into one sorted linked list and return it.

Examples:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = []
Output: []
"""

import heapq
from typing import List, Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.linked_list_utils import ListNode, build_linked_list, linked_list_to_list
from utils.test_utils import test


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Min-heap approach.

        Keep the smallest current node from each list in a heap. Each time the
        smallest node is popped, append it to the result and push its next node.

        Time Complexity: O(n log k) - n total nodes, k lists.
        Space Complexity: O(k) - Heap stores at most one node from each list.
        """
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, list_index, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, list_index, node.next))

        return dummy.next


def merge_to_list(lists):
    sol = Solution()
    return linked_list_to_list(sol.mergeKLists(lists))


if __name__ == "__main__":
    test(
        merge_to_list,
        [
            build_linked_list([1, 4, 5]),
            build_linked_list([1, 3, 4]),
            build_linked_list([2, 6]),
        ],
        [1, 1, 2, 3, 4, 4, 5, 6],
        "Test 1 - Three sorted lists",
    )
    test(merge_to_list, [], [], "Test 2 - No lists")
    test(
        merge_to_list,
        [build_linked_list([]), build_linked_list([1])],
        [1],
        "Test 3 - Empty and non-empty list",
    )

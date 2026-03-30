from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
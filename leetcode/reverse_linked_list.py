from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _prev, _next = None, head.next if head else None
        while head:
            head.next = _prev
            _prev = head
            if not _next:
                break
            head = _next
            _next = head.next
        return head

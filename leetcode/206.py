# https://leetcode.com/problems/reverse-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = None
        while head:
            current = ListNode(head.val, current)
            head = head.next
        return current


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().reverseList(head)
    while result:
        print(result.val)
        result = result.next

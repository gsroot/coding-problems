# https://leetcode.com/problems/palindrome-linked-list/
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = collections.deque()
        while head:
            q.append(head.val)
            head = head.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    result = Solution().isPalindrome(head)
    print(result)

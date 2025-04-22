# https://leetcode.com/problems/merge-two-sorted-lists/
from copy import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list3 = ListNode(list1.val, None)
            list1 = list1.next
        else:
            list3 = ListNode(list2.val, None)
            list2 = list2.next
        head = list3
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                head.next = ListNode(list1.val, None)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val, None)
                head = head.next
                list2 = list2.next
        return list3


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = Solution().mergeTwoLists(list1, list2)
    while result:
        print(result.val)
        result = result.next

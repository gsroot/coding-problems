# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()           # 결과 리스트의 가짜 머리
        tail = dummy                 # 결과 리스트의 현재 끝

        p, q = list1, list2
        while p and q:               # 둘 다 노드가 남아 있는 동안
            if p.val <= q.val:
                tail.next = p        # p가 더 작거나 같으면 p를 연결
                p = p.next
            else:
                tail.next = q        # q가 더 작으면 q를 연결
                q = q.next
            tail = tail.next         # tail을 한 칸 뒤로 이동

        # 둘 중 하나가 끝나면 남은 쪽을 그대로 연결
        tail.next = p if p else q

        return dummy.next            # 더미 다음 노드가 실제 머리


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = Solution().mergeTwoLists(list1, list2)
    while result:
        print(result.val)
        result = result.next

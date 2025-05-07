# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        p, q = l1, l2
        carry = 0

        # l1, l2, carry가 모두 소진될 때까지 반복
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0

            sum_ = x + y + carry
            carry = sum_ // 10
            digit = sum_ % 10

            current.next = ListNode(digit)
            current = current.next

            if p:
                p = p.next
            if q:
                q = q.next

        return dummy.next


if __name__ == "__main__":
    # 리스트 생성 보조 함수
    def build_list(nums):
        dummy = ListNode(0)
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    # 결과 출력 보조 함수
    def print_list(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print("[" + ",".join(vals) + "]")

    tests = [
        [
            [2, 4, 3],
            [5, 6, 4],
        ],
        [
            [0],
            [0],
        ],
    ]
    for test in tests:
        l1 = build_list(test[0])
        l2 = build_list(test[1])
        res = Solution().addTwoNumbers(l1, l2)
        print_list(res)  # 출력: [7,0,8]

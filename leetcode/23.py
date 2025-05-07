# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 결과를 이어붙일 더미 노드
        dummy = ListNode(0)
        current = dummy

        # (값, 리스트 인덱스, 노드) 형태로 최소 힙에 삽입
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            # 최소값 노드를 결과에 연결
            current.next = node
            current = current.next
            # 꺼낸 노드의 다음 노드가 있으면 힙에 다시 넣기
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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

    tests = [[[1, 4, 5], [1, 3, 4], [2, 6]], [], [[]], [[0], [1]]]
    for test in tests:
        lists = [build_list(tl) for tl in test]
        res = Solution().mergeKLists(lists)
        print_list(res)

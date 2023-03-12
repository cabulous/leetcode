import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(queue, (node.val, i, node))

        sentinel = ListNode()
        curr = sentinel

        while queue:
            _, idx, node = heapq.heappop(queue)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(queue, (node.next.val, idx, node.next))

        return sentinel.next

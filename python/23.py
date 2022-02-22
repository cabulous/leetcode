from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue(maxsize=len(lists))
        for i, first_node in enumerate(lists):
            if first_node:
                queue.put((first_node.val, i, first_node))

        sentinel = ListNode()
        curr = sentinel

        while queue.qsize() > 0:
            _, index, node = queue.get()
            curr.next = node
            curr = curr.next
            if node.next:
                queue.put((node.next.val, index, node.next))

        return sentinel.next

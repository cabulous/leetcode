from queue import PriorityQueue
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue(maxsize=len(lists))
        for i, node in enumerate(lists):
            if node:
                queue.put((node.val, i, node))

        sentinel = curr = ListNode()
        while queue.qsize() > 0:
            _, index, node = queue.get()
            curr.next = node
            curr = curr.next
            if curr.next:
                queue.put((curr.next.val, index, curr.next))

        return sentinel.next

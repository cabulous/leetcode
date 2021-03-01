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
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        sentinel = curr = ListNode()
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))
        while q.qsize() > 0:
            popped = q.get()
            index, curr.next = popped[1], popped[2]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, index, curr.next))
        return sentinel.next

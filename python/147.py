from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = head

        while curr:
            prev = sentinel
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            prev.next, curr.next, curr = curr, prev.next, curr.next

        return sentinel.next

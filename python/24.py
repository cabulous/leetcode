from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        prev = sentinel

        while head and head.next:
            first, second = head, head.next
            prev.next = second
            first.next, second.next = second.next, first

            prev = first
            head = first.next

        return sentinel.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first, second = head, head.next
        first.next, second.next = self.swapPairs(second.next), first

        return second

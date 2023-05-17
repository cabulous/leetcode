from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prev = sentinel

        while head and head.next:
            first = head
            second = head.next
            prev.next = second
            first.next, second.next = second.next, first

            prev = first
            head = first.next

        return sentinel.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first = head
        second = head.next
        first.next, second.next = self.swapPairs(second.next), first

        return second

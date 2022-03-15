from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        old_tail = head
        node_count = 1
        while old_tail.next:
            old_tail = old_tail.next
            node_count += 1

        if k % node_count == 0:
            return head

        new_tail = head
        for _ in range(node_count - k % node_count - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        old_tail.next = head
        new_tail.next = None

        return new_head

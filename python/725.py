from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        total_len = 0
        curr = head
        while curr:
            total_len += 1
            curr = curr.next

        size, remain = divmod(total_len, k)
        parts = [None] * k
        prev = None
        curr = head

        for i in range(k):
            parts[i] = curr
            curr_size = size + (1 if remain else 0)
            for __ in range(curr_size):
                prev, curr = curr, curr.next
            if prev:
                prev.next = None
            if remain:
                remain -= 1

        return parts

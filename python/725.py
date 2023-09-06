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

        res = [None] * k
        size, remain = divmod(total_len, k)
        curr = head
        prev = None

        for i in range(k):
            res[i] = curr
            curr_size = size + (1 if remain > 0 else 0)
            for j in range(curr_size):
                prev, curr = curr, curr.next
            if prev:
                prev.next = None
            if remain > 0:
                remain -= 1

        return res

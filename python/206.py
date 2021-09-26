from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre


# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        next_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return next_node

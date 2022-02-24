from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, node1: ListNode, node2: ListNode):
        sentinel = tail = ListNode()

        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                tail, node1 = node1, node1.next
            else:
                tail.next = node2
                tail, node2 = node2, node2.next

        tail.next = node1 or node2

        return sentinel.next

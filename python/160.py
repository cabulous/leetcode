from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_a = headA
        node_b = headB

        while node_a != node_b:
            node_a = headB if node_a is None else node_a.next
            node_b = headA if node_b is None else node_b.next

        return node_a

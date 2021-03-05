# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# two pointer
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        while headB:
            seen.add(headB)
            headB = headB.next
        while headA:
            if headA in seen:
                return headA
            headA = headA.next
        return None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# recursion
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


# iteration
class Solution:
    def mergeTwoLists(self, l1, l2):
        sentinel = ListNode(-1)
        prev = sentinel

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2

        return sentinel.next

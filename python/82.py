# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        sentinel = ListNode()
        sentinel.next = head
        prev = sentinel

        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return sentinel.next

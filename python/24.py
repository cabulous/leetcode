# Recursive
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second


# Iterative
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        sentinel = ListNode(-1)
        sentinel.next = head
        prev = sentinel

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return sentinel.next

# Iterative
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        return prev


# Recursive
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

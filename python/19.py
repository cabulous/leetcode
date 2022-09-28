class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

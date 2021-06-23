class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        sentinel = ListNode(0)
        sentinel.next = head
        prev = sentinel

        for i in range(left - 1):
            prev = prev.next

        tail = None
        cur = prev.next

        for i in range(right - left + 1):
            cur.next, tail, cur = tail, cur, cur.next

        prev.next.next = cur
        prev.next = tail

        return sentinel.next

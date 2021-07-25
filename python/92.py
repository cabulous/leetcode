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
        tail = sentinel

        for _ in range(left - 1):
            tail = tail.next

        pre, cur = None, tail.next

        for _ in range(right - left + 1):
            cur.next, cur, pre = pre, cur.next, cur

        tail.next.next = cur
        tail.next = pre

        return sentinel.next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first = []
        slow, fast = head, head
        while fast and fast.next:
            first.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        second = []
        while slow:
            second.append(slow.val)
            slow = slow.next

        res = 0
        for num1, num2 in zip(first, second[::-1]):
            res = max(res, num1 + num2)

        return res

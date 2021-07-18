class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        sentinel = group_tail = ListNode(0)
        sentinel.next = left = right = head

        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count < k:
                return sentinel.next
            pre, cur = right, left
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            group_tail.next, group_tail, left = pre, left, right

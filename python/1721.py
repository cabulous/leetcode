# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1009800/C%2B%2BJP3-One-Pass
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1, n2, cur = None, None, head
        while cur:
            k -= 1
            n2 = None if not n2 else n2.next
            if k == 0:
                n1 = cur
                n2 = head
            cur = cur.next
        n1.val, n2.val = n2.val, n1.val
        return head

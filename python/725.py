from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0

        for n in range(1001):
            if not cur:
                break
            cur = cur.next

        width, remainder = divmod(n, k)
        ans = []
        cur = head

        for i in range(k):
            head = write = ListNode()
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            ans.append(head.next)

        return ans

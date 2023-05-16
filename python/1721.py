from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        k -= 1
        while k > 0:
            curr = curr.next
            k -= 1

        kth_node = curr
        last_kth_node = head
        while curr.next:
            last_kth_node = last_kth_node.next
            curr = curr.next

        kth_node.val, last_kth_node.val = last_kth_node.val, kth_node.val

        return head

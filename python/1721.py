from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth_node = head
        k -= 1
        while k > 0:
            kth_node = kth_node.next
            k -= 1

        last_kth_node = head
        tail = kth_node
        while tail.next:
            last_kth_node = last_kth_node.next
            tail = tail.next

        kth_node.val, last_kth_node.val = last_kth_node.val, kth_node.val

        return head

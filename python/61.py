from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        last = head
        node_count = 1
        while last.next:
            last = last.next
            node_count += 1

        if k % node_count == 0:
            return head

        last_kth_node = head
        for i in range(node_count - k % node_count - 1):
            last_kth_node = last_kth_node.next

        new_head = last_kth_node.next
        last.next = head
        last_kth_node.next = None

        return new_head

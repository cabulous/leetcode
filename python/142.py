from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# hash table
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next

        return None


# two pointers
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        intersect = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = slow
                break

        if intersect is None:
            return None

        pointer1 = head
        pointer2 = intersect

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

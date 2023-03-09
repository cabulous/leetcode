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

        pt1 = head
        pt2 = intersect
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next

        return pt1

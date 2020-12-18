# hash table
class Solution:
    def detectCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


# two pointers
class Solution:
    def detectCycle(self, head):
        def getIntersect(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None

        if not head:
            return None

        intersect = getIntersect(head)

        if not intersect:
            return None

        ptr1 = head
        ptr2 = intersect

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

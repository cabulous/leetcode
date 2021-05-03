# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Copy into Array List and then Use Two Pointer Technique
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values == values[::-1]


# Reverse Second Half In-place O(1) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        res = True
        first_position = head
        second_position = second_half_start

        while res and second_position:
            if first_position.val != second_position.val:
                res = False
                break
            first_position = first_position.next
            second_position = second_position.next

        first_half_end.next = self.reverse_list(second_half_start)
        return res

    def end_of_first_half(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

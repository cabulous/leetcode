# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Copy into Array List and then Use Two Pointer Technique
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values == values[::-1]


# Reverse Second Half In-place O(1) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        before_end = self.before_end(head)
        after_head = self.reverse_list(before_end.next)

        res = True
        ptr1 = head
        ptr2 = after_head

        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                res = False
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        before_end.next = self.reverse_list(after_head)

        return res

    def before_end(self, node):
        slow = fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, node):
        prev = None
        curr = node
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

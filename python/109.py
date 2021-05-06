# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Inorder Simulation
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        size = self.find_size(head)

        def convert(lo, hi):
            nonlocal head
            if lo > hi:
                return None
            mi = lo + (hi - lo) // 2
            left = convert(lo, mi - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mi + 1, hi)
            return node

        return convert(0, size - 1)

    def find_size(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt


# Recursion + Conversion to Array
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        values = self.map_list_to_values(head)

        def convert_list_to_bst(lo, hi):
            if lo > hi:
                return None
            mi = lo + (hi - lo) // 2
            node = TreeNode(values[mi])
            if lo == hi:
                return node
            node.left = convert_list_to_bst(lo, mi - 1)
            node.right = convert_list_to_bst(mi + 1, hi)
            return node

        return convert_list_to_bst(0, len(values) - 1)

    def map_list_to_values(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values


# Recursion
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.find_middle(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def find_middle(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow

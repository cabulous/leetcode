from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.vals = []

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        self.vals = self.list_to_values(head)

        return self.convert(0, len(self.vals) - 1)

    def convert(self, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(self.vals[mid])

        if left == right:
            return node

        node.left = self.convert(left, mid - 1)
        node.right = self.convert(mid + 1, right)

        return node

    def list_to_values(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        curr = root
        while curr:
            if curr.left:
                right_most = curr.left
                while right_most.right:
                    right_most = right_most.right
                right_most.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

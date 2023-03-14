from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.preorder(root, 0)
        return self.res

    def preorder(self, node, total):
        if not node:
            return

        total = total * 10 + node.val

        if not node.left and not node.right:
            self.res += total

        self.preorder(node.left, total)
        self.preorder(node.right, total)

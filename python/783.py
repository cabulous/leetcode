from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.prev = None
        self.res = float('inf')

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if self.prev:
            self.res = min(self.res, node.val - self.prev.val)
        self.prev = node

        self.inorder(node.right)

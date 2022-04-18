from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for val in self.inorder(root):
            k -= 1
            if k == 0:
                return val

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)

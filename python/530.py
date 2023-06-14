from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.array = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return min(b - a for a, b in zip(self.array, self.array[1:]))

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.array.append(node.val)
        if node.right:
            self.inorder(node.right)

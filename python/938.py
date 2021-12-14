from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.helper(root, low, high)

    def helper(self, node, low, high):
        if node is None:
            return 0

        left = self.helper(node.left, low, high)
        right = self.helper(node.right, low, high)

        if low <= node.val <= high:
            return left + right + node.val

        return left + right

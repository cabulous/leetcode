from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if self.is_leaf(node.left):
                total += node.left.val
            stack.append(node.left)
            stack.append(node.right)

        return total

    def is_leaf(self, node: Optional[TreeNode]):
        return node is not None and node.left is None and node.right is None

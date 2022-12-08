from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return list(self.helper(root1)) == list(self.helper(root2))

    def helper(self, node):
        if node:
            if node.left is None and node.right is None:
                yield node.val
            yield from self.helper(node.left)
            yield from self.helper(node.right)

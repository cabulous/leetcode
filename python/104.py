from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node):
        if node is None:
            return 0

        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)

        return 1 + max(left_depth, right_depth)

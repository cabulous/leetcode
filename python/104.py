from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

    def helper(self, node):
        if node is None:
            return 0

        left_depth = self.helper(node.left)
        right_depth = self.helper(node.right)

        return 1 + max(left_depth, right_depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = deque([(root, 1)])
        res = 1

        while stack:
            node, depth = stack.popleft()
            res = max(res, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return res

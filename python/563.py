from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.total

    def helper(self, node):
        if not node:
            return 0

        left_sum = self.helper(node.left)
        right_sum = self.helper(node.right)
        tilt = abs(left_sum - right_sum)
        self.total += tilt

        return left_sum + right_sum + node.val

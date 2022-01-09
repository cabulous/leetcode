from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.helper(root)
        return int(self.res)

    def helper(self, node):
        if not node:
            return 0

        left_max = max(self.helper(node.left), 0)
        right_max = max(self.helper(node.right), 0)
        curr_max = left_max + node.val + right_max

        self.res = max(self.res, curr_max)

        return node.val + max(left_max, right_max)

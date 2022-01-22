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
        self.helper(root)
        return int(self.res)

    def helper(self, node):
        if not node:
            return 0

        left_sum = max(self.helper(node.left), 0)
        right_sum = max(self.helper(node.right), 0)
        curr_sum = left_sum + node.val + right_sum

        self.res = max(self.res, curr_sum)

        return node.val + max(left_sum, right_sum)

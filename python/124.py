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
        if node is None:
            return 0

        left_sum = max(0, self.helper(node.left))
        right_sum = max(0, self.helper(node.right))
        curr_sum = left_sum + node.val + right_sum

        self.res = max(self.res, curr_sum)

        return node.val + max(left_sum, right_sum)

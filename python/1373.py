import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return 0, True, -math.inf, math.inf

        left_sum, left_valid, left_max, left_min = self.traverse(node.left)
        right_sum, right_valid, right_max, right_min = self.traverse(node.right)

        if left_valid and right_valid and left_max < node.val < right_min:
            total = left_sum + right_sum + node.val
            self.res = max(self.res, total)
            return total, True, max(right_max, node.val), min(left_min, node.val)

        return 0, False, -math.inf, math.inf

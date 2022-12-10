from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.all_sums = []

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7

        total = self.tree_sum(root)
        res = 0

        for sub_total in self.all_sums:
            res = max(res, sub_total * (total - sub_total))

        return res % mod

    def tree_sum(self, node):
        if not node:
            return 0

        left_sum = self.tree_sum(node.left)
        right_sum = self.tree_sum(node.right)
        total = left_sum + node.val + right_sum
        self.all_sums.append(total)

        return total

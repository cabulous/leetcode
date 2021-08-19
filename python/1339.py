from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7
        all_sums = []

        def tree_sum(sub_root):
            if not sub_root:
                return 0
            left_sum = tree_sum(sub_root.left)
            right_sum = tree_sum(sub_root.right)
            total_sum = left_sum + sub_root.val + right_sum
            all_sums.append(total_sum)
            return total_sum

        total = tree_sum(root)
        res = 0

        for s in all_sums:
            res = max(res, s * (total - s))

        return res % mod

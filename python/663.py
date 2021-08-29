from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
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
        all_sums.pop()

        return total / 2.0 in all_sums

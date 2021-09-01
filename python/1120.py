from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/maximum-average-subtree/discuss/334120/Python-Recursion
class Solution:
    def __init__(self):
        self.res = 0

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.helper(root)
        return self.res

    def helper(self, sub_root):
        if not sub_root:
            return [0, 0.0]

        node_count_left, tree_sum_left = self.helper(sub_root.left)
        node_count_right, tree_sum_right = self.helper(sub_root.right)

        node_count = node_count_left + node_count_right + 1
        tree_sum = tree_sum_left + sub_root.val + tree_sum_right

        self.res = max(self.res, tree_sum / node_count)

        return [node_count, tree_sum]

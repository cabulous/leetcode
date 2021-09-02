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
        if not root:
            return 0

        self.helper(root)
        return self.res

    def helper(self, sub_root):
        if not sub_root:
            return [0, 0.0]

        left_node_count, left_sum = self.helper(sub_root.left)
        right_node_count, right_sum = self.helper(sub_root.right)

        total_node_count = left_node_count + right_node_count + 1
        total_sum = left_sum + sub_root.val + right_sum
        self.res = max(self.res, total_sum / total_node_count)

        return [total_node_count, total_sum]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, root.val, root.val)

    def helper(self, node, curr_max, curr_min):
        if node is None:
            return curr_max - curr_min

        next_max = max(curr_max, node.val)
        next_min = min(curr_min, node.val)

        left_diff = self.helper(node.left, next_max, next_min)
        right_diff = self.helper(node.right, next_max, next_min)

        return max(left_diff, right_diff)

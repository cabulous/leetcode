from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root, root.val, root.val)

    def helper(self, node, cur_max, cur_min):
        if not node:
            return cur_max - cur_min

        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)

        left_diff = self.helper(node.left, cur_max, cur_min)
        right_diff = self.helper(node.right, cur_max, cur_min)

        return max(left_diff, right_diff)

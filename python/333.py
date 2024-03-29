from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]

    def dfs(self, node):
        if not node:
            return 0, float('inf'), float('-inf')

        left_count, left_min, left_max = self.dfs(node.left)
        right_count, right_min, right_max = self.dfs(node.right)

        is_valid_bst = left_max < node.val < right_min

        if is_valid_bst:
            return left_count + right_count + 1, min(node.val, left_min), max(node.val, right_max)

        return max(left_count, right_count), float('-inf'), float('inf')

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/solutions/531867/java-python-dfs-solution/?orderBy=most_votes
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        _, _, res = self.dfs(root)
        return res

    def dfs(self, node):
        if not node:
            return -1, -1, -1

        left_left, left_right, left_res = self.dfs(node.left)
        right_left, right_right, right_res = self.dfs(node.right)

        return [
            left_right + 1,
            right_left + 1,
            max(left_right + 1, right_left + 1, left_res, right_res),
        ]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]

        res = []
        for mid in range(start, end + 1):
            left_trees = self.helper(start, mid - 1)
            right_trees = self.helper(mid + 1, end)
            for left in left_trees:
                for right in right_trees:
                    res.append(TreeNode(mid, left, right))

        return res

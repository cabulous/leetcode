from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_level = 1
        res = curr_level

        level = [root]
        curr_max = root.val
        while level:
            curr_level += 1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            if level:
                total = sum(node.val for node in level)
                if total > curr_max:
                    curr_max = total
                    res = curr_level

        return res

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        level = [root]
        left_to_right = True
        while level:
            curr = [node.val for node in level]
            res.append(curr)
            left_to_right = not left_to_right
            if left_to_right:
                level = [kid for node in reversed(level) for kid in [node.left, node.right] if kid]
            else:
                level = [kid for node in reversed(level) for kid in [node.right, node.left] if kid]

        return res

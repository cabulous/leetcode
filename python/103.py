from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        level = [root]
        is_left_to_right = True
        res = []

        while level:
            res.append([node.val for node in level])
            is_left_to_right = not is_left_to_right
            if is_left_to_right:
                level = [kid for node in reversed(level) for kid in (node.left, node.right) if kid]
            else:
                level = [kid for node in reversed(level) for kid in (node.right, node.left) if kid]

        return res

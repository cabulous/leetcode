from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = deque([(root, 0)])
        res = 0

        while level:
            __, head_pos = level[0]
            __, tail_pos = level[-1]
            res = max(res, tail_pos - head_pos + 1)

            for _ in range(len(level)):
                node, pos = level.popleft()
                if node.left:
                    level.append((node.left, pos * 2))
                if node.right:
                    level.append((node.right, pos * 2 + 1))

        return res

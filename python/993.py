from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/cousins-in-binary-tree/discuss/654172/Python-Straight-Forward-BFS-and-DFS-Solutions
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []
        queue = deque([(root, 0, None)])

        while queue:
            if len(res) == 2:
                break
            node, depth, parent = queue.popleft()
            if node.val in (x, y):
                res.append((depth, parent))
            if node.left:
                queue.append((node.left, depth + 1, node))
            if node.right:
                queue.append((node.right, depth + 1, node))

        (x_depth, x_parent), (y_depth, y_parent) = res

        return x_depth == y_depth and x_parent != y_parent

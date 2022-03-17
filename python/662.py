from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        res = 0

        while queue:
            _, head_position = queue[0]
            _, tail_position = queue[-1]
            res = max(res, tail_position - head_position + 1)
            for _ in range(len(queue)):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, position * 2))
                if node.right:
                    queue.append((node.right, position * 2 + 1))

        return res


class Solution:

    def __init__(self):
        self.depth_to_head_position = {}
        self.res = 0

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, 0)
        return self.res

    def dfs(self, node, depth, position):
        if node is None:
            return

        if depth not in self.depth_to_head_position:
            self.depth_to_head_position[depth] = position

        self.res = max(self.res, position - self.depth_to_head_position[depth] + 1)

        self.dfs(node.left, depth + 1, position * 2)
        self.dfs(node.right, depth + 1, position * 2 + 1)

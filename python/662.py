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
        self.res = 0
        self.first_col_index_table = {}

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, 0)
        return self.res

    def dfs(self, node, depth, col_index):
        if node is None:
            return

        if depth not in self.first_col_index_table:
            self.first_col_index_table[depth] = col_index

        self.res = max(self.res, col_index - self.first_col_index_table[depth] + 1)

        self.dfs(node.left, depth + 1, col_index * 2)
        self.dfs(node.right, depth + 1, col_index * 2 + 1)

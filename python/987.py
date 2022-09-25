from typing import List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, col = queue.popleft()
            if node:
                node_list.append((col, row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        res = defaultdict(list)
        for col, _, val in sorted(node_list):
            res[col].append(val)

        return [res[col] for col in sorted(res)]

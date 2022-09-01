from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [cols[i] for i in sorted(cols)]


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = 0
        max_col = 0

        while queue:
            node, idx = queue.popleft()
            if node is not None:
                cols[idx].append(node.val)
                min_col = min(min_col, idx)
                max_col = max(max_col, idx)
                queue.append((node.left, idx - 1))
                queue.append((node.right, idx + 1))

        return [cols[i] for i in range(min_col, max_col + 1)]

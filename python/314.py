from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, idx = queue.popleft()
            if node is not None:
                cols[idx].append(node.val)
                queue.append((node.left, idx - 1))
                queue.append((node.right, idx + 1))

        return [cols[i] for i in sorted(cols)]

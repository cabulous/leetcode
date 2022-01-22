from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return root

        curr_level = deque([root])

        while curr_level:
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                if node == u:
                    return curr_level.popleft() if curr_level else None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level = next_level

        return None

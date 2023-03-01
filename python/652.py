from collections import Counter
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = Counter()
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        self.encode(root)
        return self.res

    def encode(self, node):
        if not node:
            return ''

        left = self.encode(node.left)
        right = self.encode(node.right)
        curr = str(node.val)

        encoded = f'{curr}#{left}#{right}'
        self.count[encoded] += 1

        if self.count[encoded] == 2:
            self.res.append(node)

        return encoded

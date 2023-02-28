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

    def encode(self, root):
        if not root:
            return ''

        left = self.encode(root.left)
        right = self.encode(root.right)
        curr = str(root.val)

        encoded = f'{curr}#{left}#{right}'
        self.count[encoded] += 1

        if self.count[encoded] == 2:
            self.res.append(root)

        return encoded

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/discuss/74576/13-lines-of-Python-DFS-solution
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = deque([(root, 1)])
        while queue:
            node, count = queue.popleft()
            res = max(res, count)
            if node.left:
                queue.append((node.left, count + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                queue.append((node.right, count + 1 if node.right.val == node.val + 1 else 1))

        return res


class Solution:

    def __init__(self):
        self.res = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return 0

        inr = 1

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.left and node.left.val == node.val + 1:
            inr = max(inr, left + 1)
        if node.right and node.right.val == node.val + 1:
            inr = max(inr, right + 1)

        self.res = max(self.res, inr)

        return inr

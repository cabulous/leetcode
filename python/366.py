from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return -1
        height = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if height >= len(self.res):
            self.res.append([])
        self.res[height].append(node.val)
        return height

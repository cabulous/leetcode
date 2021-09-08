import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, -math.inf)]

        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                res += 1
            max_so_far = max(max_so_far, node.val)
            if node.left:
                stack.append((node.left, max_so_far))
            if node.right:
                stack.append((node.right, max_so_far))

        return res


class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -math.inf)
        return self.res

    def dfs(self, node, max_so_far):
        if node.val >= max_so_far:
            self.res += 1
        max_so_far = max(max_so_far, node.val)
        if node.left:
            self.dfs(node.left, max_so_far)
        if node.right:
            self.dfs(node.right, max_so_far)

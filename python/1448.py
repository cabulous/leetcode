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
            if node.left:
                stack.append((node.left, max(node.val, max_so_far)))
            if node.right:
                stack.append((node.right, max(node.val, max_so_far)))

        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, max_so_far):
            nonlocal res
            if node.val >= max_so_far:
                res += 1
            if node.left:
                dfs(node.left, max(max_so_far, node.val))
            if node.right:
                dfs(node.right, max(max_so_far, node.val))

        dfs(root, -math.inf)

        return res

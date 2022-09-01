from collections import deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        queue = deque([(root, -math.inf)])
        while queue:
            node, max_so_far = queue.popleft()
            if node.val >= max_so_far:
                res += 1

            max_so_far = max(max_so_far, node.val)
            if node.left:
                queue.append((node.left, max_so_far))
            if node.right:
                queue.append((node.right, max_so_far))

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

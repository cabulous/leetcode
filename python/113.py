from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:

    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.dfs(root, targetSum, [])
        return self.res

    def dfs(self, node, remain, path):
        if node is None:
            return

        path.append(node.val)
        remain -= node.val

        if node.left is None and node.right is None and remain == 0:
            self.res.append(path[:])
        else:
            self.dfs(node.left, remain, path)
            self.dfs(node.right, remain, path)

        path.pop()


# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
# bfs
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = deque([(root, root.val, [root.val])])

        while queue:
            node, curr_sum, path = queue.popleft()
            if node.left is None and node.right is None and curr_sum == targetSum:
                res.append(path)
            if node.left:
                queue.append((node.left, curr_sum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val, path + [node.right.val]))

        return res

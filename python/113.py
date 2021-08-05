from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, node, remaining_sum, path, res):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and remaining_sum == node.val:
            res.append(list(path))
        else:
            self.dfs(node.left, remaining_sum - node.val, path, res)
            self.dfs(node.right, remaining_sum - node.val, path, res)

        path.pop()


# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
# bfs
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([(root, root.val, [root.val])])

        while queue:
            node, cur_sum, path = queue.popleft()
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path)
            if node.left:
                queue.append((node.left, cur_sum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, cur_sum + node.right.val, path + [node.right.val]))

        return res

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/105127/%22one-liner%22
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        level = [root]
        while level:
            res.append(sum(node.val for node in level) / len(level))
            level = [kid for node in level for kid in [node.left, node.right] if kid]
        return res


# https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/105108/Python-Straightforward-with-Explanation
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        d = defaultdict(list)

        def dfs(node, depth):
            if node:
                d[depth].append(node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return [sum(d[level]) / len(d[level]) for level in sorted(d)]

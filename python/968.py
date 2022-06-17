# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
class Solution:

    def __init__(self):
        self.res = 0

    def minCameraCover(self, root: TreeNode) -> int:
        ret = self.dfs(root)
        return self.res + (ret == 0)

    def dfs(self, node):
        if node is None:
            return 2

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left == 0 or right == 0:
            self.res += 1
            return 1

        if left == 1 or right == 1:
            return 2

        return 0


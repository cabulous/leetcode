# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                res += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0

        return (dfs(root) == 0) + res


# dp
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(node):
            if not node:
                return 0, 0, float('inf')
            left = solve(node.left)
            right = solve(node.right)
            dp0 = left[1] + right[1]
            dp1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            dp2 = 1 + min(left) + min(right)
            return dp0, dp1, dp2

        return min(solve(root)[1:])


# greedy
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        covered = {None}

        def dfs(node, parent=None):
            nonlocal ans
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (parent is None and node not in covered) or (node.left not in covered) or (
                        node.right not in covered):
                    ans += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)

        return ans

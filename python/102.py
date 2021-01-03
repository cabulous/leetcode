from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) -> [[int]]:
        if not root:
            return []

        queue = deque([root, None, ])
        ans = []
        intermediate = []
        while queue:
            node = queue.popleft()
            if node:
                intermediate.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                ans.append(intermediate[:])
                intermediate.clear()
                if queue:
                    queue.append(None)

        return ans


# dfs
class Solution:
    def levelOrder(self, root) -> [[int]]:
        if not root:
            return []

        levels = []

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

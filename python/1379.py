# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# inorder travers
from collections import deque


class Solution:
    def getTargetCopy(self, original, cloned, target):
        ans = None

        def inorder(o, c):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    nonlocal ans
                    ans = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        return ans


# bfs
class Solution:
    def getTargetCopy(self, original, cloned, target):
        queue_o = deque([original, ])
        queue_c = deque([cloned, ])

        while queue_o:
            node_o = queue_o.popleft()
            node_c = queue_c.popleft()
            if node_o is target:
                return node_c
            if node_o:
                queue_o.append(node_o.left)
                queue_o.append(node_o.right)
                queue_c.append(node_c.left)
                queue_c.append(node_c.right)

        return None

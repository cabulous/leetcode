# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


#  BST
class Solution:
    def isValidBST(self, root) -> bool:
        def bst(node, lo=-math.inf, hi=math.inf):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return bst(node.left, lo, node.val) and bst(node.right, node.val, hi)
        return bst(root)


# Traveral
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lo, hi = stack.pop()
            if not root:
                continue
            val = root.val
            if val >= lo or val >= hi:
                return False
            stack.append((root.right, val, hi))
            stack.append((root.left, lo, val))
        return True


# inorder
class Solution:
    def isValidBST(self, root) -> bool:
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        self.prev = -math.inf
        return inorder(root)

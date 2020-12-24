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
            node, lo, hi = stack.pop()
            if not node:
                continue
            if node.val <= lo or node.val >= hi:
                return False
            stack.append((node.left, lo, node.val))
            stack.append((node.right, node.val, hi))
        return True


# inorder
class Solution:
    def __init__(self):
        self.prev = -math.inf

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

        return inorder(root)

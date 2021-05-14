# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


# dfs
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.helper(root)

    def helper(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        left_tail = self.helper(node.left)
        right_tail = self.helper(node.right)
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        return right_tail if right_tail else left_tail


# stack
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None

        start, end = 1, 2
        tail = None
        stack = deque([(root, start)])

        while stack:
            curr, recursion_state = stack.pop()
            if not curr.left and not curr.right:
                tail = curr
                continue
            if recursion_state == start:
                if curr.left:
                    stack.append((curr, end))
                    stack.append((curr.left, start))
                elif curr.right:
                    stack.append((curr.right, start))
            else:
                right = curr.right
                if tail:
                    tail.right = curr.right
                    curr.right = curr.left
                    curr.left = None
                    right = tail.right
                if right:
                    stack.append((right, start))


# Iterative
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None

        node = root

        while node:
            if node.left:
                right_most = node.left
                while right_most.right:
                    right_most = right_most.right
                right_most.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

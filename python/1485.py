from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:

    def __init__(self):
        self.memo = {}

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return None

        if node in self.memo:
            return self.memo[node]

        copy_node = NodeCopy(node.val)
        self.memo[node] = copy_node

        copy_node.left = self.dfs(node.left)
        copy_node.right = self.dfs(node.right)
        copy_node.random = self.dfs(node.random)

        return copy_node

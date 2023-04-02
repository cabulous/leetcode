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
        return self.clone(root)

    def clone(self, node):
        if node is None:
            return None

        if node in self.memo:
            return self.memo[node]

        clone_node = NodeCopy(node.val)
        self.memo[node] = clone_node

        clone_node.left = self.clone(node.left)
        clone_node.right = self.clone(node.right)
        clone_node.random = self.clone(node.random)

        return clone_node

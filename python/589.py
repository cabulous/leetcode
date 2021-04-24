from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# dfs
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []

        def dfs(node: Node):
            if not node:
                return
            res.append(node.val)
            if node.children:
                for kid in node.children:
                    dfs(kid)

        dfs(root)
        return res


# stack
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])

        return res

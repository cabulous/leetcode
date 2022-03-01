from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])
        clone = {root: Node(root.val)}

        while queue:
            node = queue.popleft()
            if node.children:
                for kid in node.children:
                    clone[kid] = Node(kid.val)
                    clone[node].children.append(clone[kid])
                    queue.append(kid)

        return clone[root]


class Solution:

    def __init__(self):
        self.memo = {}

    def cloneTree(self, root: 'Node') -> 'Node':
        return self.dfs(root)

    def dfs(self, node: 'Node'):
        if not node:
            return None

        if node in self.memo:
            return self.memo[node]

        self.memo[node] = Node(node.val)

        if node.children:
            for kid in node.children:
                clone = self.dfs(kid)
                self.memo[node].children.append(clone)

        return self.memo[node]

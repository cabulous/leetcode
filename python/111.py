from collections import deque


# recursion
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        children = [root.left, root.right]
        if not any(children):
            return 1

        res = float('inf')
        for kid in children:
            if kid:
                res = min(res, self.minDepth(kid))

        return res + 1


# dfs
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        res = float('inf')

        while stack:
            node, depth = stack.pop()
            children = [node.left, node.right]
            if not any(children):
                res = min(res, depth)
            for kid in children:
                if kid:
                    stack.append((kid, depth + 1))

        return res


# bfs
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for kid in children:
                if kid:
                    queue.append((kid, depth + 1))

        return -1

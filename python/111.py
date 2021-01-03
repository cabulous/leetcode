# recursion
from collections import deque


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        children = [root.left, root.right]
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(min_depth, self.minDepth(c))

        return min_depth + 1


# dfs
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        stack = [(1, root), ]
        min_depth = float('inf')

        while stack:
            depth, node = stack.pop()
            children = [node.left, node.right]
            if not any(children):
                min_depth = min(min_depth, depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth


# bfs
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        queue = deque([(1, root), ])

        while queue:
            depth, node = queue.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((depth + 1, c))

        return -1

from collections import namedtuple


class Solution:
    def subtreeWithAllDeepest(self, root):
        Result = namedtuple("Result", ("node", "depth"))

        def dfs(node):
            if not node:
                return Result(None, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            if left.depth > right.depth:
                return Result(left.node, left.depth + 1)
            elif left.depth < right.depth:
                return Result(right.node, right.depth + 1)
            else:
                return Result(node, left.depth + 1)

        return dfs(root).node

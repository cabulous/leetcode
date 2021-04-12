# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = [root]
        prev_level = []
        while level:
            prev_level = level
            level = [kid for node in level for kid in [node.left, node.right] if kid]

        return sum(node.val for node in prev_level)


# Iterative DFS Preorder Traversal
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        deepest_sum = depth = 0
        stack = [(root, 0)]

        while stack:
            node, curr_depth = stack.pop()
            if not node.left and not node.right:
                if curr_depth > depth:
                    deepest_sum = node.val
                    depth = curr_depth
                elif curr_depth == depth:
                    deepest_sum += node.val
            else:
                if node.left:
                    stack.append((node.left, curr_depth + 1))
                if node.right:
                    stack.append((node.right, curr_depth + 1))

        return deepest_sum

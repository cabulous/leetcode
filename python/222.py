from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = self.compute_depth(root)
        if depth == 0:
            return 1

        left, right = 0, 2 ** depth - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** depth - 1) + left

    def compute_depth(self, node):
        res = 0
        while node.left:
            node = node.left
            res += 1
        return res

    def exists(self, idx, depth, node):
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

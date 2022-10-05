from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        sentinel = TreeNode(val, root)
        level = [sentinel]

        for _ in range(depth - 1):
            level = [kid for node in level for kid in [node.left, node.right] if kid]

        for node in level:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)

        return sentinel.left


# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS/689369
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None or depth == 0:
            return None

        if depth == 1:
            return TreeNode(val, root)

        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
            return root

        root.left = self.addOneRow(root.left, val, depth - 1)
        root.right = self.addOneRow(root.right, val, depth - 1)
        return root

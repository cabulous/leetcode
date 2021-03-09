# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        sentinel = TreeNode(v, root)
        level = [sentinel]
        for _ in range(d - 1):
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        for node in level:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return sentinel.left


# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS/689369
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root or d <= 0:
            return None
        if d == 1:
            return TreeNode(v, root, None)
        if d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1)
        return root

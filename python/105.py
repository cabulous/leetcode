from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.preorder = []
        self.preorder_idx = 0
        self.inorder_map = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder

        for i, val in enumerate(inorder):
            self.inorder_map[val] = i

        return self.helper(0, len(preorder) - 1)

    def helper(self, left, right):
        if left > right:
            return None

        val = self.preorder[self.preorder_idx]
        self.preorder_idx += 1

        node = TreeNode(val)
        node.left = self.helper(left, self.inorder_map[val] - 1)
        node.right = self.helper(self.inorder_map[val] + 1, right)

        return node

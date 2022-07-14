from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.inorder_idx_map = {}
        self.preorder_idx = 0
        self.preorder = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder

        for idx, value in enumerate(inorder):
            self.inorder_idx_map[value] = idx

        return self.array_to_tree(0, len(preorder) - 1)

    def array_to_tree(self, left, right):
        if left > right:
            return None

        root_val = self.preorder[self.preorder_idx]
        root = TreeNode(root_val)

        self.preorder_idx += 1

        root.left = self.array_to_tree(left, self.inorder_idx_map[root_val] - 1)
        root.right = self.array_to_tree(self.inorder_idx_map[root_val] + 1, right)

        return root

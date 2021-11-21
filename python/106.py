from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.postorder = []
        self.idx_map = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder = postorder
        self.idx_map = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(0, len(inorder) - 1)

    def helper(self, idx_left, idx_right):
        if idx_left > idx_right:
            return None

        val = self.postorder.pop()
        root = TreeNode(val)

        idx = self.idx_map[val]

        root.right = self.helper(idx + 1, idx_right)
        root.left = self.helper(idx_left, idx - 1)

        return root

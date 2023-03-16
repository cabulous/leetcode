from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.postorder = []
        self.lookup = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder = postorder
        for i, val in enumerate(inorder):
            self.lookup[val] = i

        return self.helper(0, len(inorder) - 1)

    def helper(self, left, right):
        if left > right:
            return None

        val = self.postorder.pop()
        node = TreeNode(val)
        idx = self.lookup[val]

        node.right = self.helper(idx + 1, right)
        node.left = self.helper(left, idx - 1)

        return node

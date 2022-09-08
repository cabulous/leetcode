from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return []

        res = []
        res.extend(self.inorderTraversal(node.left))
        res.append(node.val)
        res.extend(self.inorderTraversal(node.right))

        return res

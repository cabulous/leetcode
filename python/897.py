class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sentinel = TreeNode()
        curr = sentinel

        for val in self.inorder(root):
            curr.right = TreeNode(val)
            curr = curr.right

        return sentinel.right

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)

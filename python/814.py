class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return root if self.contains_one(root) else None

    def contains_one(self, node):
        if not node:
            return False

        left_contains_one = self.contains_one(node.left)
        right_contains_one = self.contains_one(node.right)

        if not left_contains_one:
            node.left = None
        if not right_contains_one:
            node.right = None

        return node.val == 1 or left_contains_one or right_contains_one

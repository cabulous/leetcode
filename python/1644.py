class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root, p, q)
        return self.res

    def helper(self, node, p, q):
        if node is None:
            return 0

        curr = 1 if node in (p, q) else 0
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)

        count = curr + left + right
        if count == 2 and self.res is None:
            self.res = node

        return count

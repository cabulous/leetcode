class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.p = None
        self.q = None
        self.res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.find(root)

        return self.res

    def find(self, node):
        if node is None:
            return False

        found_left = self.find(node.left)
        found_right = self.find(node.right)
        found = node in (self.p, self.q)

        if found + found_left + found_right >= 2:
            self.res = node

        return found or found_left or found_right


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = [self.lowestCommonAncestor(kid, p, q) for kid in [root.left, root.right]]
        return root if left and right else left or right

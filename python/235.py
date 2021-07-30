class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val, p_val, q_val = root.val, p.val, q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)

        if p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        node = root

        while node:
            node_val = node.val
            if p_val > node_val and q_val > node_val:
                node = node.right
            elif p_val < node_val and q_val < node_val:
                node = node.left
            else:
                return node
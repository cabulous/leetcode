# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# general solution
class Solution:
    def __init__(self):
        self.prev = None
        self.successor = None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            left_most = p.right
            while left_most.left:
                left_most = left_most.left
            self.successor = left_most
        else:
            self.inorder(root, p)
        return self.successor

    def inorder(self, node, p):
        if not node:
            return
        self.inorder(node.left, p)
        if self.prev == p and not self.successor:
            self.successor = node
            return
        self.prev = node
        self.inorder(node.right, p)


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor


# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72721/10-(and-4)-lines-O(h)-JavaC++/201050
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode', last_left=None) -> 'TreeNode':
        if not root:
            return last_left
        return self.inorderSuccessor(root.left, p, root) if root.val > p.val else self.inorderSuccessor(root.right, p,
                                                                                                        last_left)

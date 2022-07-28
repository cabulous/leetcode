from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/subtree-of-another-tree/discuss/102729/Short-Python-by-converting-into-strings
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.serialize(subRoot) in self.serialize(root)

    def serialize(self, root: Optional[TreeNode]) -> str:
        return '^' + str(root.val) + '#' + self.serialize(root.left) + self.serialize(root.right) if root else '$'


# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_match(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_match(self, node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
        if not (node_a and node_b):
            return node_a is node_b
        return (
                node_a.val == node_b.val
                and self.is_match(node_a.left, node_b.left)
                and self.is_match(node_a.right, node_b.right)
        )

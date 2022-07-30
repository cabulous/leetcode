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

    def serialize(self, root):
        return '^' + str(root.val) + '#' + self.serialize(root.left) + self.serialize(root.right) if root else '$'

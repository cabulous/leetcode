from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res

    def helper(self, sub_root):
        if not sub_root:
            return 0

        left_count = self.helper(sub_root.left)
        right_count = self.helper(sub_root.right)
        self.res = max(self.res, left_count + right_count)

        return 1 + max(left_count, right_count)

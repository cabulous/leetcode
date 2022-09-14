class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = 1

    def longestConsecutive(self, root: TreeNode) -> int:
        self.longest_path(root)
        return self.res

    def longest_path(self, node):
        if node is None:
            return 0, 0

        inr, dcr = 1, 1

        if node.left:
            left_inr, left_dcr = self.longest_path(node.left)
            if node.val == node.left.val - 1:
                inr = max(inr, left_inr + 1)
            elif node.val == node.left.val + 1:
                dcr = max(dcr, left_dcr + 1)

        if node.right:
            right_inr, right_dcr = self.longest_path(node.right)
            if node.val == node.right.val - 1:
                inr = max(inr, right_inr + 1)
            elif node.val == node.right.val + 1:
                dcr = max(dcr, right_dcr + 1)

        self.res = max(self.res, inr + dcr - 1)

        return inr, dcr

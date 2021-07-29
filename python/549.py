class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_val = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.longest_path(root)
        return self.max_val

    def longest_path(self, node):
        if not node:
            return [0, 0]

        inr = dcr = 1

        if node.left:
            left = self.longest_path(node.left)
            if node.val == node.left.val - 1:
                inr = left[0] + 1
            elif node.val == node.left.val + 1:
                dcr = left[1] + 1

        if node.right:
            right = self.longest_path(node.right)
            if node.val == node.right.val - 1:
                inr = max(inr, right[0] + 1)
            elif node.val == node.right.val + 1:
                dcr = max(dcr, right[1] + 1)

        self.max_val = max(self.max_val, inr + dcr - 1)

        return [inr, dcr]

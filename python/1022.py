from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        res = 0

        while stack:
            node, cur_num = stack.pop()
            cur_num = (cur_num << 1) | node.val
            if node.left is None and node.right is None:
                res += cur_num
            if node.left:
                stack.append((node.left, cur_num))
            if node.right:
                stack.append((node.right, cur_num))

        return res


class Solution:

    def __init__(self):
        self.res = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.res

    def helper(self, node, cur_num):
        cur_num = (cur_num << 1) | node.val
        if node.left is None and node.right is None:
            self.res += cur_num
        if node.left:
            self.helper(node.left, cur_num)
        if node.right:
            self.helper(node.right, cur_num)

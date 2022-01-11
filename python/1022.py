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
            if node is not None:
                cur_num = (cur_num << 1) | node.val
                if node.left is None and node.right is None:
                    res += cur_num
                else:
                    stack.append((node.left, cur_num))
                    stack.append((node.right, cur_num))

        return res


class Solution:

    def __init__(self):
        self.nums = []

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.helper(root, 0)
        return sum(self.nums)

    def helper(self, node, cur_num):
        cur_num = (cur_num << 1) + node.val
        if node.left is None and node.right is None:
            self.nums.append(cur_num)
            return
        if node.left is not None:
            self.helper(node.left, cur_num)
        if node.right is not None:
            self.helper(node.right, cur_num)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, 0)]

        while stack:
            node, cur_sum = stack.pop()
            if node is None:
                continue
            cur_sum = cur_sum * 10 + node.val
            if node.left is None and node.right is None:
                total += cur_sum
            stack.append((node.left, cur_sum))
            stack.append((node.right, cur_sum))

        return total


class Solution:
    def __init__(self):
        self.total = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.preorder(root, 0)
        return self.total

    def preorder(self, node, cur_sum):
        if node is None:
            return

        cur_sum = cur_sum * 10 + node.val

        if node.left is None and node.right is None:
            self.total += cur_sum

        self.preorder(node.left, cur_sum)
        self.preorder(node.right, cur_sum)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = curr_sum = 0

        while root:
            if root.left:
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1
                if predecessor.right is None:
                    curr_sum = curr_sum * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:
                    if predecessor.left is None:
                        total += curr_sum
                    for _ in range(steps):
                        curr_sum //= 10
                    predecessor.right = None
                    root = root.right
            else:
                curr_sum = curr_sum * 10 + root.val
                if root.right is None:
                    total += curr_sum
                root = root.right

        return total

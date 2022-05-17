from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274621/JavaC%2B%2BPython-Iterative-Stack-Solution
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0

        while index < len(traversal):
            level = 0
            val = ''

            while index < len(traversal) and traversal[index] == '-':
                level += 1
                index += 1

            while index < len(traversal) and traversal[index] != '-':
                val += traversal[index]
                index += 1

            while len(stack) > level:
                stack.pop()

            node = TreeNode(int(val))

            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# best
# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation/271108
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        root, _ = self.helper(s, 0)
        return root

    def helper(self, s, i):
        n = len(s)
        start = i
        while i < n and (s[i] == '-' or s[i].isdigit()):
            i += 1
        node = TreeNode(int(s[start:i]))
        if i < n and s[i] == '(':
            i += 1
            node.left, i = self.helper(s, i)
            i += 1
        if i < n and s[i] == '(':
            i += 1
            node.right, i = self.helper(s, i)
            i += 1
        return node, i


# recursion
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        return self.dfs(s, 0)[0]

    def get_number(self, s, index):
        is_negative = False
        if s[index] == '-':
            is_negative = True
            index += 1

        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1

        return -number if is_negative else number, index

    def dfs(self, s, index):
        if index == len(s):
            return None, index

        value, index = self.get_number(s, index)
        node = TreeNode(value)

        if index < len(s) and s[index] == '(':
            node.left, index = self.dfs(s, index + 1)

        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self.dfs(s, index + 1)

        return node, index + 1 if index < len(s) and s[index] == ')' else index


# stack - not so good
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None

        n = len(s)
        root = TreeNode()
        stack = [root]
        index = 0

        while index < n:
            node = stack.pop()

            if s[index].isdigit() or s[index] == '-':
                value, index = self.get_number(s, index)
                node.val = value

                if index < n and s[index] == '(':
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)

            elif node.left and s[index] == '(':
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)

            index += 1

        return stack.pop() if stack else root

    def get_number(self, s, index):
        is_negative = False

        if s[index] == '-':
            is_negative = True
            index += 1

        number = 0

        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1

        return -number if is_negative else number, index

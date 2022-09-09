from collections import deque


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/864596/Python-Standard-parser-implementation
class Solution:
    def expTree(self, s: str) -> 'Node':
        tokens = deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens: deque):
        left = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in '+-':
            op = tokens.popleft()
            right = self.parse_term(tokens)
            left = Node(op, left, right)
        return left

    def parse_term(self, tokens: deque):
        left = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in '*/':
            op = tokens.popleft()
            right = self.parse_factor(tokens)
            left = Node(op, left, right)
        return left

    def parse_factor(self, tokens: deque):
        while len(tokens) > 0 and tokens[0] == '(':
            tokens.popleft()
            node = self.parse_expression(tokens)
            tokens.popleft()
            return node
        token = tokens.popleft()
        return Node(token)

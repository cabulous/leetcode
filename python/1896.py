# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/discuss/1267304/Python-Recursion-dfs-solution-explained
class Solution:

    def __init__(self):
        self.expression = ''
        self.d = {}

    def minOperationsToFlip(self, expression: str) -> int:
        self.expression = expression
        self.d = self.correct(expression)
        return self.dfs(0, len(expression) - 1)[1]

    def correct(self, s):
        stack = []
        d = {}
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                last = stack.pop()
                d[i] = last
        return d

    def dfs(self, start, end):
        if start == end:
            return int(self.expression[start]), 1

        start2 = self.d.get(end, end)
        if start2 == start:
            return self.dfs(start + 1, end - 1)

        val1, change1 = self.dfs(start, start2 - 2)
        val2, change2 = self.dfs(start2, end)
        op = self.expression[start2 - 1]

        t = {
            '|': lambda x, y: x | y,
            '&': lambda x, y: x & y,
        }

        change3 = 1 if val1 + val2 == 1 else min(change1, change2) + (val1 ^ (op == '&'))

        return t[op](val1, val2), change3

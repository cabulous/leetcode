# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    res[i] = ''

        while stack:
            res[stack.pop()] = ''

        return ''.join(res)

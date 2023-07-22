# https://leetcode.com/problems/ternary-expression-parser/solutions/1454722/python3-2-approaches/
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        for ch in reversed(expression):
            if stack and stack[-1] == '?':
                stack.pop()
                t = stack.pop()
                f = stack.pop()
                if ch == 'T':
                    stack.append(t)
                elif ch == 'F':
                    stack.append(f)
            elif ch != ':':
                stack.append(ch)

        return stack[-1]

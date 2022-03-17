# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                if not stack:
                    return False
                if stack[-1] != valid_parentheses[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0

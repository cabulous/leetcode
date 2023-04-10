# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                if not stack:
                    return False
                prev = stack.pop()
                if valid_parentheses[ch] != prev:
                    return False
            else:
                stack.append(ch)

        return not stack

# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                if not stack:
                    return False
                expected = valid_parentheses[ch]
                if expected != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

# https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        res = []

        for ch in s:
            if ch == '(' and opened > 0:
                res.append(ch)
            elif ch == ')' and opened > 1:
                res.append(ch)
            opened += 1 if ch == '(' else -1

        return ''.join(res)

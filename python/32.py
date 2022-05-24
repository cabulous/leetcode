class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        res = 0

        for i in range(1, n):
            if s[i] == ')':
                if i - 1 >= 0 and s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                res = max(res, dp[i])

        return res


# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)

        return res


# left + right scan
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right * 2)
            elif right > left:
                left = right = 0

        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right * 2)
            elif left > right:
                left = right = 0

        return res

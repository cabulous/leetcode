# dp
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        max_ans = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i >= 2 else 0)
                elif i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                max_ans = max(max_ans, dp[i])

        return max_ans


# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        max_ans = 0
        stack = [-1]
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_ans = max(max_ans, i - stack[-1])
                else:
                    stack.append(i)
        return max_ans


# left + right scan
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        max_ans = 0
        left, right = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_ans = max(max_ans, 2 * right)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in reversed(range(n)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_ans = max(max_ans, 2 * right)
            elif left > right:
                left, right = 0, 0
        return max_ans

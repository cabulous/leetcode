from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


class Solution:

    def __init__(self):
        self.s = ''

    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        return self.dp(0, len(s) - 1)

    @lru_cache(None)
    def dp(self, left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if self.s[left] == self.s[right]:
            return self.dp(left + 1, right - 1) + 2
        return max(self.dp(left + 1, right), self.dp(left, right - 1))

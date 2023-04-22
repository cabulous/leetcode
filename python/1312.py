class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                dp[i + 1][j - 1] = dp[i][j] + 1 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])

        return len(s) - dp[-1][-1]

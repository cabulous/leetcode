class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, ch1 in enumerate(text1):
            for j, ch2 in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if ch1 == ch2 else max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]

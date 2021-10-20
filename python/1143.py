# https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                dp[i + 1][j + 1] = dp[i][j] + 1 if c1 == c2 else max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]

# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470706/JavaC%2B%2BPython-Longest-Common-Sequence
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i + 1][j], dp[i][j + 1])

        return n - dp[n][n]

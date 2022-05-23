# https://leetcode.com/problems/palindromic-substrings/discuss/105707/Java-Python-DP-solution-based-on-longest-palindromic-substring
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0

        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                dp[start][end] = s[start] == s[end] and (end - start + 1 < 3 or dp[start + 1][end - 1])
                res += dp[start][end]

        return res

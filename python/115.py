class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {}

        def unique_subsequences(i=0, j=0):
            if i == m or j == n or m - i < n - j:
                return int(j == n)

            if (i, j) in memo:
                return memo[i, j]

            ans = unique_subsequences(i + 1, j)

            if s[i] == t[j]:
                ans += unique_subsequences(i + 1, j + 1)

            memo[i, j] = ans

            return ans

        return unique_subsequences()


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = 0
        for i in range(m + 1):
            dp[i][n] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        for i in reversed(range(m)):
            prev = 1
            for j in reversed(range(n)):
                old_dpj = dp[j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = old_dpj

        return dp[0]

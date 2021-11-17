class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]

        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

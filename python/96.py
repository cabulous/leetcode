class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]


class Solution:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(0, n):
            c = c * 2 * (2 * i + 1) / (i + 2)
        return int(c)

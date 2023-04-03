class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(len(dp)):
            dp[i] = i
            for j in range(1, i - 3):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[-1]

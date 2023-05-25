class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [1.0] + [0.0] * n
        total = 1.0

        for point in range(1, n + 1):
            dp[point] = total / maxPts
            if point < k:
                total += dp[point]
            if point - maxPts >= 0:
                total -= dp[point - maxPts]

        return sum(dp[k:])

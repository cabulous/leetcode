class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        pivot = n
        least = k
        max_gain = maxPts

        if least == 0 or pivot >= least + max_gain:
            return 1.0

        dp = [1.0] + [0.0] * pivot
        probability = 1.0

        for point in range(1, pivot + 1):
            dp[point] = probability / max_gain
            if point < least:
                probability += dp[point]
            if point - max_gain >= 0:
                probability -= dp[point - max_gain]

        return sum(dp[least:])

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        max_point = n
        least = k
        max_gain = maxPts

        if least == 0 or max_point >= least + max_gain:
            return 1.0

        dp = [1.0] + [0.0] * max_point
        acc_prob = 1.0

        for point in range(1, max_point + 1):
            dp[point] = acc_prob / max_gain
            if point < least:
                acc_prob += dp[point]
            if point - max_gain >= 0:
                acc_prob -= dp[point - max_gain]

        return sum(dp[least:])

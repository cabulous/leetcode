from collections import Counter

MOD = 10 ** 9 + 7


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter({0: 1})

        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % MOD

        res = sum(dp[i] for i in range(low, high + 1)) % MOD

        return res

MOD = 10 ** 9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        last = {}

        for i, ch in enumerate(s):
            dp.append(dp[-1] * 2)
            if ch in last:
                dp[-1] -= dp[last[ch]]
            last[ch] = i

        return (dp[-1] - 1) % MOD

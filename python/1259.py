class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (numPeople // 2 + 1)
        dp[0] = 1

        for i in range(1, numPeople // 2 + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
                dp[i] %= mod

        return dp[-1]


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        res = 1
        for i in range(1, numPeople // 2 + 1):
            res *= (numPeople - i + 1)
            res //= i

        mod = 10 ** 9 + 7
        return res // (numPeople // 2 + 1) % mod

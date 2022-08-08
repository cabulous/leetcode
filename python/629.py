MOD = 10 ** 9 + 7


# https://leetcode.com/problems/k-inverse-pairs-array/discuss/104824/Python-concise-solution
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1

        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                if j >= i:
                    dp[j] -= dp[j - i]

        return dp[k] % MOD

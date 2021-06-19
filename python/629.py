# https://leetcode.com/problems/k-inverse-pairs-array/discuss/104824/Python-concise-solution
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [1] + [0] * k

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                dp[j] -= j - i >= 0 and dp[j - i]

        return dp[k] % modulo


# https://leetcode.com/problems/k-inverse-pairs-array/discuss/282586/Python-376ms-A-less-confusing-cumulative-sum-approach
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            cum_sum = 0
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                    cum_sum += 1
                else:
                    cum_sum += dp[i - 1][j]
                    if j - i >= 0:
                        cum_sum -= dp[i - 1][j - i]
                    dp[i][j] = cum_sum % modulo

        return dp[-1][-1]

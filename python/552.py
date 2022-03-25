MOD = 10 ** 9 + 7


# https://leetcode.com/problems/student-attendance-record-ii/discuss/101634/Python-DP-with-explanation/105313
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 3

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

        res = dp[n]

        for i in range(1, n + 1):
            res += dp[i - 1] * dp[n - i] % MOD

        res %= MOD

        return res

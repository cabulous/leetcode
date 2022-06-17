from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for zero, one in [self.count(s) for s in strs]:
            for zero_max in range(m, -1, -1):
                for one_max in range(n, -1, -1):
                    if zero <= zero_max and one <= one_max:
                        dp[zero_max][one_max] = max(dp[zero_max][one_max], 1 + dp[zero_max - zero][one_max - one])

        return dp[m][n]

    def count(self, s):
        return sum(c == '0' for c in s), sum(c == '1' for c in s)

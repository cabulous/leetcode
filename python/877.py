from typing import List
from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (j - i - n) % 2
            if parity == 1:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, n - 1) > 0


# https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

        return dp[0][-1] > 0


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0

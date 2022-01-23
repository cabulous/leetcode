from functools import lru_cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for k in range(1, int(i ** 0.5) + 1):
                if not dp[i - k * k]:
                    dp[i] = True
                    break

        return dp[-1]


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return self.dfs(n)

    @lru_cache(None)
    def dfs(self, remain):
        if remain == 0:
            return False

        for i in range(1, int(remain ** 0.5) + 1):
            if not self.dfs(remain - i * i):
                return True

        return False

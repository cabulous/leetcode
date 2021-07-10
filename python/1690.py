from functools import lru_cache
from itertools import accumulate
from typing import List


# https://leetcode.com/problems/stone-game-vii/discuss/970363/Python-Top-Down-and-Bottom-Up-DP-explained
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sum = [0] + list(accumulate(stones))
        n = len(stones)
        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n)):
            for j in range(i + 1, n):
                dp[i][j] = max(self.score(pre_sum, i + 1, j) - dp[i + 1][j], self.score(pre_sum, i, j - 1) - dp[i][j - 1])

        return dp[0][-1]

    def score(self, pre_sum, start, end):
        return pre_sum[end + 1] - pre_sum[start]


# https://leetcode.com/problems/stone-game-vii/discuss/1264544/Python-O(n*n)-dp-solution-how-to-avoid-TLE-explained
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0] + list(accumulate(stones))

        @lru_cache(2000)
        def score(i, j):
            if i > j:
                return 0
            sm = presum[j + 1] - presum[i]
            return sm - min(stones[i] + score(i + 1, j), stones[j] + score(i, j - 1))

        res = score(0, len(stones) - 1)
        score.cache_clear()

        return res

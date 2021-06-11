from functools import lru_cache
from itertools import accumulate
from typing import List


# https://leetcode.com/problems/stone-game-vii/discuss/970363/Python-Top-Down-and-Bottom-Up-DP-explained
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sum = [0] + list(accumulate(stones))

        def score(i, j):
            return pre_sum[j + 1] - pre_sum[i]

        n = len(stones)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(score(i + 1, j) - dp[i + 1][j], score(i, j - 1) - dp[i][j - 1])

        return dp[0][-1]


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

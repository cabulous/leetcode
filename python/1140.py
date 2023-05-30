from functools import lru_cache

import copy


class Solution:

    def __init__(self):
        self.dp = []

    def stoneGameII(self, piles: list[int]) -> int:
        self.dp = copy.deepcopy(piles)
        for i in range(len(self.dp) - 2, -1, -1):
            self.dp[i] += self.dp[i + 1]
        return self.helper(0, 1)

    @lru_cache(None)
    def helper(self, idx, max_pile):
        if idx + 2 * max_pile >= len(self.dp):
            return self.dp[idx]
        return self.dp[idx] - min(
            self.helper(idx + x, max(max_pile, x))
            for x in range(1, 2 * max_pile + 1)
        )

from functools import lru_cache


class Solution:

    def __init__(self):
        self.piles = []

    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        self.piles = piles
        return self.dp(0, k)

    @lru_cache(None)
    def dp(self, pile_idx, remain):
        if pile_idx == len(self.piles):
            return 0
        if remain == 0:
            return 0

        curr = 0
        res = self.dp(pile_idx + 1, remain)

        coin_count = min(remain, len(self.piles[pile_idx]))
        for coin_idx in range(coin_count):
            curr += self.piles[pile_idx][coin_idx]
            res = max(res, curr + self.dp(pile_idx + 1, remain - 1 - coin_idx))

        return res

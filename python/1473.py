import math
from functools import lru_cache
from typing import List


# https://leetcode.com/problems/paint-house-iii/discuss/674485/Python-Solution
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0}
        next_dp = {}

        for i, painted_color in enumerate(houses):
            available_colors = range(1, n + 1) if painted_color == 0 else [painted_color]
            for next_color in available_colors:
                for color, block in dp:
                    next_block = block + (color != next_color)
                    if next_block <= target:
                        next_dp[next_color, next_block] = min(
                            next_dp.get((next_color, next_block), math.inf),
                            dp[color, block] + (cost[i][next_color - 1] if next_color != painted_color else 0)
                        )
            dp, next_dp = next_dp, {}

        return min([dp[c, b] for c, b in dp if b == target] or [-1])


class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0
        self.target = 0
        self.houses = []
        self.cost = []

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.m = m
        self.n = n
        self.target = target
        self.houses = houses
        self.cost = cost

        res = self.dfs(0, 0, -1)

        return res if res < math.inf else -1

    @lru_cache(None)
    def dfs(self, house_idx, block_count, color):
        if house_idx == self.m and block_count == self.target:
            return 0
        if house_idx >= self.m or block_count > self.target:
            return math.inf

        res = math.inf
        if self.houses[house_idx] != 0:
            res = min(
                res,
                self.dfs(house_idx + 1, block_count + (self.houses[house_idx] != color), self.houses[house_idx])
            )
        else:
            for next_color in range(1, self.n + 1):
                res = min(
                    res,
                    self.cost[house_idx][next_color - 1] + self.dfs(house_idx + 1, block_count + (next_color != color),
                                                                    next_color)
                )

        return res

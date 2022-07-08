import math
from functools import lru_cache
from typing import List


# https://leetcode.com/problems/paint-house-iii/discuss/674485/Python-Solution
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp1 = {(0, 0): 0}
        dp2 = {}

        for index, house in enumerate(houses):
            colors = range(1, n + 1) if house == 0 else [house]
            for painted_color in colors:
                for color, block in dp1:
                    new_block_count = block + (color != painted_color)
                    if new_block_count > target:
                        continue
                    dp2[painted_color, new_block_count] = min(
                        dp2.get((painted_color, new_block_count), math.inf),
                        dp1[color, block] + (cost[index][painted_color - 1] if painted_color != house else 0),
                    )
            dp1, dp2 = dp2, {}

        return min([dp1[color, block] for color, block in dp1 if block == target] or [-1])


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

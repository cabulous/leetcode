import copy
from functools import lru_cache


class Solution:

    def __init__(self):
        self.costs = []
        self.colors = []

    def minCostII(self, costs: list[list[int]]) -> int:
        self.costs = costs
        self.colors = list(range(len(costs[0])))

        res = float('inf')
        for color in self.colors:
            res = min(res, self.dfs(0, color))

        return res

    @lru_cache(None)
    def dfs(self, house, color):
        cost = self.costs[house][color]
        if house == len(self.costs) - 1:
            return cost

        best = float('inf')
        for next_color in self.colors:
            if next_color != color:
                best = min(best, self.dfs(house + 1, next_color))

        return cost + best


class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        dp = copy.deepcopy(costs)

        for house in range(1, len(costs)):
            for color in range(len(costs[0])):
                best = float('inf')
                for prev_color in range(len(costs[0])):
                    if prev_color != color:
                        best = min(best, dp[house - 1][prev_color])
                dp[house][color] += best

        return min(dp[-1])

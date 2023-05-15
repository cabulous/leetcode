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
    def dfs(self, idx, color):
        cost = self.costs[idx][color]
        if idx == len(self.costs) - 1:
            return cost

        next_cost = float('inf')
        for next_color in self.colors:
            if next_color == color:
                continue
            next_cost = min(next_cost, self.dfs(idx + 1, next_color))

        return cost + next_cost


class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        dp = copy.deepcopy(costs)

        for house in range(1, len(dp)):
            for color in range(len(dp[0])):
                best = float('inf')
                for prev_color in range(len(dp[0])):
                    if prev_color == color:
                        continue
                    best = min(best, dp[house - 1][prev_color])
                dp[house][color] += best

        return min(dp[-1])

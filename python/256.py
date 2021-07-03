import copy
from functools import lru_cache
from typing import List


# memoization
class Solution:
    def __init__(self):
        self.costs = []

    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        self.costs = costs
        return min(self.paint_cost(0, 0), self.paint_cost(0, 1), self.paint_cost(0, 2))

    @lru_cache(2000)
    def paint_cost(self, house_idx, color):
        cost = self.costs[house_idx][color]
        if house_idx == len(self.costs) - 1:
            pass
        elif color == 0:
            cost += min(self.paint_cost(house_idx + 1, 1), self.paint_cost(house_idx + 1, 2))
        elif color == 1:
            cost += min(self.paint_cost(house_idx + 1, 0), self.paint_cost(house_idx + 1, 2))
        elif color == 2:
            cost += min(self.paint_cost(house_idx + 1, 0), self.paint_cost(house_idx + 1, 1))
        return cost


# dp
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        for n in reversed(range(len(costs) - 1)):
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        return min(costs[0])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev = costs[-1]

        for n in reversed(range(len(costs) - 1)):
            curr = copy.deepcopy(costs[n])
            curr[0] += min(prev[1], prev[2])
            curr[1] += min(prev[0], prev[2])
            curr[2] += min(prev[0], prev[1])
            prev = curr

        return min(prev)


# https://leetcode.com/problems/paint-house/discuss/68209/1%2B-lines-Ruby-Python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        cols = len(costs[0])
        prev = [0] * cols

        for curr in costs:
            prev = [curr[i] + min(prev[:i] + prev[i + 1:]) for i in range(cols)]

        return min(prev)

import copy
from functools import lru_cache, reduce
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

    @lru_cache(maxsize=None)
    def paint_cost(self, house_idx, color):
        total_cost = self.costs[house_idx][color]

        if house_idx == len(self.costs) - 1:
            pass
        elif color == 0:
            total_cost += min(self.paint_cost(house_idx + 1, 1), self.paint_cost(house_idx + 1, 2))
        elif color == 1:
            total_cost += min(self.paint_cost(house_idx + 1, 0), self.paint_cost(house_idx + 1, 2))
        elif color == 2:
            total_cost += min(self.paint_cost(house_idx + 1, 0), self.paint_cost(house_idx + 1, 1))

        return total_cost


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

        prev_row = costs[-1]

        for n in reversed(range(len(costs) - 1)):
            curr_row = copy.deepcopy(costs[n])
            curr_row[0] += min(prev_row[1], prev_row[2])
            curr_row[1] += min(prev_row[0], prev_row[2])
            curr_row[2] += min(prev_row[0], prev_row[1])
            prev_row = curr_row

        return min(prev_row)


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

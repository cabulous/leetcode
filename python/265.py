import math
from typing import List
from functools import lru_cache


# memoization
class Solution:
    def __init__(self):
        self.costs = []
        self.k = 0

    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        self.costs = costs
        self.k = len(costs[0])
        cost = math.inf

        for color in range(self.k):
            cost = min(cost, self.paint_house(0, color))

        return cost

    @lru_cache(None)
    def paint_house(self, house_idx, color):
        cost = self.costs[house_idx][color]
        if house_idx == len(self.costs) - 1:
            return cost
        next_cost = math.inf
        for next_color in range(self.k):
            if next_color == color:
                continue
            next_cost = min(next_cost, self.paint_house(house_idx + 1, next_color))
        return cost + next_cost


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])

        for house in range(1, n):
            for color in range(k):
                best = math.inf
                for prev_color in range(k):
                    if prev_color == color:
                        continue
                    best = min(best, costs[house - 1][prev_color])
                costs[house][color] += best

        return min(costs[-1])


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])

        for house in range(1, n):
            min_color = second_min_color = None
            for color in range(k):
                cost = costs[house - 1][color]
                if min_color is None or cost < costs[house - 1][min_color]:
                    min_color, second_min_color = color, min_color
                elif second_min_color is None or cost < costs[house - 1][second_min_color]:
                    second_min_color = color
            for color in range(k):
                if color == min_color:
                    costs[house][color] += costs[house - 1][second_min_color]
                else:
                    costs[house][color] += costs[house - 1][min_color]

        return min(costs[-1])


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        prev_min_cost = prev_second_min_cost = prev_min_color = None

        for color, cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_cost = cost
                prev_min_color = color
            elif prev_second_min_cost is None or cost < prev_second_min_cost:
                prev_second_min_cost = cost

        for house in range(1, n):
            min_cost = second_min_cost = min_color = None
            for color in range(k):
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost
                if min_cost is None or cost < min_cost:
                    second_min_cost = min_cost
                    min_cost = cost
                    min_color = color
                elif second_min_cost is None or cost < second_min_cost:
                    second_min_cost = cost
            prev_second_min_cost = second_min_cost
            prev_min_cost = min_cost
            prev_min_color = min_color

        return prev_min_cost

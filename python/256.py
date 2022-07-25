import copy
from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.costs = []

    def minCost(self, costs: List[List[int]]) -> int:
        if not any(costs):
            return 0

        self.costs = costs

        return min(
            self.helper(0, 0),
            self.helper(0, 1),
            self.helper(0, 2),
        )

    @lru_cache(None)
    def helper(self, house_idx, color):
        cost = self.costs[house_idx][color]

        if house_idx == len(self.costs) - 1:
            return cost

        if color == 0:
            cost += min(self.helper(house_idx + 1, 1), self.helper(house_idx + 1, 2))
        elif color == 1:
            cost += min(self.helper(house_idx + 1, 0), self.helper(house_idx + 1, 2))
        elif color == 2:
            cost += min(self.helper(house_idx + 1, 0), self.helper(house_idx + 1, 1))

        return cost


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not any(costs):
            return 0

        curr = copy.deepcopy(costs)
        for i in range(len(curr) - 2, -1, -1):
            curr[i][0] += min(curr[i + 1][1], curr[i + 1][2])
            curr[i][1] += min(curr[i + 1][0], curr[i + 1][2])
            curr[i][2] += min(curr[i + 1][0], curr[i + 1][1])

        return min(curr[0])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not any(costs):
            return 0

        prev = costs[-1]
        for i in range(len(costs) - 2, -1, -1):
            curr = costs[i].copy()
            curr[0] += min(prev[1], prev[2])
            curr[1] += min(prev[0], prev[2])
            curr[2] += min(prev[0], prev[1])
            prev = curr

        return min(prev)

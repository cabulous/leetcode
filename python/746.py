from functools import lru_cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one = min_cost[i - 1] + cost[i - 1]
            take_two = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one, take_two)

        return min_cost[-1]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = curr = 0
        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
        return curr


class Solution:

    def __init__(self):
        self.cost = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        return self.helper(len(cost))

    @lru_cache(None)
    def helper(self, n):
        if n <= 1:
            return 0
        return min(
            self.helper(n - 1) + self.cost[n - 1],
            self.helper(n - 2) + self.cost[n - 2],
        )

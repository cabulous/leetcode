from functools import lru_cache
from typing import List


# dp bottom-up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            take_one = min_cost[i - 1] + cost[i - 1]
            take_two = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one, take_two)
        return min_cost[-1]


# bottom-up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = prev = 0
        for i in range(2, len(cost) + 1):
            curr, prev = min(curr + cost[i - 1], prev + cost[i - 2]), curr
        return curr


# dp top-down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def min_cost(n):
            if n <= 1:
                return 0
            return min(cost[n - 1] + min_cost(n - 1), cost[n - 2] + min_cost(n - 2))

        return min_cost(len(cost))

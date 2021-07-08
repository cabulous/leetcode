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
        prev = curr = 0
        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
        return curr


# dp top-down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(2000)
        def helper(n):
            if n <= 1:
                return 0
            return min(helper(n - 1) + cost[n - 1], helper(n - 2) + cost[n - 2])

        return helper(len(cost))

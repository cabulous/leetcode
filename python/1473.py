import math
from typing import List


# https://leetcode.com/problems/paint-house-iii/discuss/674485/Python-Solution
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0}

        for i, painted_color in enumerate(houses):
            next_dp = {}
            available_colors = range(1, n + 1) if painted_color == 0 else [painted_color]

            for next_color in available_colors:
                for (color, block), curr_cost in dp.items():
                    next_block = block + (color != next_color)
                    if next_block <= target:
                        next_dp[next_color, next_block] = min(
                            next_dp.get((next_color, next_block), math.inf),
                            curr_cost + (cost[i][next_color - 1] if next_color != painted_color else 0),
                        )

            dp = next_dp

        return min([dp[c, b] for c, b in dp if b == target] or [-1])

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        half = len(costs) // 2
        res = 0

        for i in range(half):
            res += costs[i][0] + costs[i + half][1]

        return res

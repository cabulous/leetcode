from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        curr_max_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                curr_max_time = 0
            res += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        return res

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        curr_max_time = 0

        for i in range(len(colors)):
            if i > 0 and colors[i - 1] != colors[i]:
                curr_max_time = 0
            res += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        return res

import bisect
from typing import List


# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        dp = [[0, 0]]

        for start, end, profit in jobs:
            i = bisect.bisect(dp, [start + 1]) - 1
            if dp[i][1] + profit > dp[-1][1]:
                dp.append([end, dp[i][1] + profit])

        return dp[-1][1]

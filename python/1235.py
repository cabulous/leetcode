import bisect
from typing import List


# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        dp = [[0, 0]]

        for start, end, curr_profit in jobs:
            i = bisect.bisect_right(dp, [start + 1]) - 1
            total_so_far = dp[i][1] + curr_profit
            if total_so_far > dp[-1][1]:
                dp.append([end, total_so_far])

        return dp[-1][1]

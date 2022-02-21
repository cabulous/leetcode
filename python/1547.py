from typing import List


# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/discuss/781074/JavaC%2B%2BPython-Merge-Stones
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        cuts_count = len(cuts)
        dp = [[0] * cuts_count for _ in range(cuts_count)]

        for d in range(2, cuts_count):
            for i in range(cuts_count - d):
                dp[i][i + d] = min(dp[i][j] + dp[j][i + d] for j in range(i + 1, i + d)) + cuts[i + d] - cuts[i]

        return dp[0][-1]

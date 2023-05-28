from typing import List


# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/discuss/781074/JavaC%2B%2BPython-Merge-Stones
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])

        dp = [[0] * len(cuts) for _ in range(len(cuts))]
        for d in range(2, len(cuts)):
            for i in range(len(cuts) - d):
                dp[i][i + d] = min(
                    dp[i][j] + dp[j][i + d] for j in range(i + 1, i + d)
                ) + cuts[i + d] - cuts[i]

        return dp[0][-1]

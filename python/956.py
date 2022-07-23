from collections import defaultdict
from typing import List


# https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0

        for next_height in rods:
            next_dp = dp.copy()
            for diff, height in dp.items():
                next_dp[diff + next_height] = max(next_dp[diff + next_height], height)
                next_dp[abs(diff - next_height)] = max(next_dp[abs(diff - next_height)],
                                                       height + min(diff, next_height))
            dp = next_dp

        return dp[0]

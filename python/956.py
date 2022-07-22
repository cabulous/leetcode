from collections import defaultdict
from typing import List


# https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0

        for height in rods:
            next_dp = dp.copy()
            for delta, curr_height in dp.items():
                next_dp[height + delta] = max(next_dp[height + delta], curr_height)
                next_dp[abs(height - delta)] = max(next_dp[abs(height - delta)], curr_height + min(height, delta))
            dp = next_dp

        return dp[0]
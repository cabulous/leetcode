from collections import Counter


# https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = Counter({0: 0})

        for delta in rods:
            next_dp = dp.copy()
            for diff, height in dp.items():
                next_dp[diff + delta] = max(next_dp[diff + delta], height)
                next_dp[abs(diff - delta)] = max(next_dp[abs(diff - delta)], height + min(diff, delta))
            dp = next_dp

        return dp[0]

from typing import List


# https://leetcode.com/problems/binary-trees-with-factors/discuss/125794/C%2B%2BJavaPython-DP-solution
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        for a in sorted(arr):
            dp[a] = 1 + sum(dp[b] * dp.get(a // b, 0) for b in dp if a % b == 0)

        return sum(dp.values()) % mod

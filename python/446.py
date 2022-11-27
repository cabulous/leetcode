from typing import List
from collections import Counter


# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [Counter() for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
            res += sum(dp[i].values())

        return res - (n - 1) * n // 2

from typing import List
from collections import Counter


# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [Counter() for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
            ans += sum(dp[i].values())

        return ans - (n - 1) * n // 2

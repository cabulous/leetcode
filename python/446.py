from typing import List
from collections import Counter


# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [Counter() for _ in range(len(nums))]
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
            res += sum(dp[i].values())

        return res - (len(nums) - 1) * len(nums) // 2

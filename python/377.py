from typing import List
from functools import lru_cache


class Solution:

    def __init__(self):
        self.nums = []

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = sorted(nums)
        return self.helper(target)

    @lru_cache(None)
    def helper(self, target):
        if target == 0:
            return 1

        res = 0
        for num in self.nums:
            if target < num:
                return res
            res += self.helper(target - num)

        return res


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        nums.sort()

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum < num:
                    break
                dp[comb_sum] += dp[comb_sum - num]

        return dp[target]

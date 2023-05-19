from functools import lru_cache

import math


class Solution:

    def __init__(self):
        self.nums = []

    def maxScore(self, nums: list[int]) -> int:
        self.nums = nums
        return self.dfs(1, 0)

    @lru_cache(None)
    def dfs(self, idx, mask):
        if idx > len(self.nums) // 2:
            return 0

        res = 0
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                curr_mask = (1 << i) + (1 << j)
                if not mask & curr_mask:
                    res = max(
                        res,
                        idx * math.gcd(self.nums[i], self.nums[j]) + self.dfs(idx + 1, mask + curr_mask),
                    )

        return res

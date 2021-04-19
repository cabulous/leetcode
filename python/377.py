from typing import List
from functools import lru_cache


# Top-Down Dynamic Programming
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def combs(remain):
            if remain == 0:
                return 1
            res = 0
            for num in nums:
                if remain - num >= 0:
                    res += combs(remain - num)
                else:
                    break
            return res

        return combs(target)


# Bottom-Up Dynamic Programming
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]
                else:
                    break

        return dp[target]

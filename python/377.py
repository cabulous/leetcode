class Solution:

    def __init__(self):
        self.memo = {}
        self.nums = []

    def combinationSum4(self, nums: list[int], target: int) -> int:
        self.nums = sorted(nums)
        return self.helper(target)

    def helper(self, target):
        if target == 0:
            return 1

        if target in self.memo:
            return self.memo[target]

        res = 0
        for num in self.nums:
            if target - num < 0:
                self.memo[target] = res
                return self.memo[target]
            res += self.helper(target - num)

        self.memo[target] = res
        return self.memo[target]


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [1] + [0] * target
        for comb_sum in range(1, target + 1):
            for num in sorted(nums):
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]
        return dp[-1]

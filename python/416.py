from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        dp = [True] + [False] * subset_sum

        for num in nums:
            for i in reversed(range(num, subset_sum + 1)):
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]

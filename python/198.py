from typing import List


class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        return self.rob_from(0, nums)

    def rob_from(self, i, nums):
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        self.memo[i] = max(self.rob_from(i + 1, nums), self.rob_from(i + 2, nums) + nums[i])

        return self.memo[i]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev2, prev1 = 0, nums[0]

        for num in nums[1:]:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1

from typing import List


class Solution:

    def __init__(self):
        self.nums = []
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.helper(0)

    def helper(self, idx):
        if len(self.nums) <= idx:
            return 0

        if idx in self.memo:
            return self.memo[idx]

        self.memo[idx] = max(self.helper(idx + 1), self.helper(idx + 2) + self.nums[idx])

        return self.memo[idx]


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, nums[0]

        for num in nums[1:]:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1

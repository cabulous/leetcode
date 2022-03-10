import math
from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/discuss/819326/Python-in-6-short-lines-with-easy-explanation
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        return (self.helper(nums) - 1) % MOD

    def helper(self, nums):
        if len(nums) <= 2:
            return 1

        root_val = nums[0]
        left = [v for v in nums if v < root_val]
        right = [v for v in nums if v > root_val]

        return math.comb(len(left) + len(right), len(right)) * self.helper(left) * self.helper(right)

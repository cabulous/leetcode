from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sub = max_sub = nums[0]
        for num in nums[1:]:
            curr_sub = max(num, curr_sub + num)
            max_sub = max(max_sub, curr_sub)
        return max_sub

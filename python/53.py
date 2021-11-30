from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sub = max_sub = nums[0]

        for num in nums[1:]:
            cur_sub = max(num, cur_sub + num)
            max_sub = max(max_sub, cur_sub)

        return max_sub

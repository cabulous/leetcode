from typing import List


# https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/3066034/python3-dp-two-passes-for-beginners-with-explanations/
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_sub = nums[0]
        min_sub = 0
        res = nums[0]

        for num in nums[1:]:
            max_sub = max(max_sub + num, num)
            min_sub = min(min_sub + num, num)
            res = max(res, max_sub, total - min_sub)

        return res

from typing import List


# https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation/859294
class Solution:

    def __init__(self):
        self.nums = []
        self.cut_max = 0

    def splitArray(self, nums: List[int], m: int) -> int:
        self.nums = nums
        self.cut_max = m

        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_split(self, sum_max):
        curr = 0
        cut = 0
        for num in self.nums:
            if curr + num > sum_max:
                cut += 1
                curr = 0
            curr += num
        return cut < self.cut_max

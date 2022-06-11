import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        curr = sum(nums)
        res = math.inf
        left = 0

        for right in range(len(nums)):
            curr -= nums[right]
            while curr < x and left <= right:
                curr += nums[left]
                left += 1
            if curr == x:
                res = min(res, len(nums) - (right - left + 1))

        return res if res < math.inf else -1


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        length = self.min_operation_sub_array(nums, total - x)

        return len(nums) - length if length != -1 else -1

    def min_operation_sub_array(self, nums, target):
        curr = 0
        left = 0
        res = -1

        for right in range(len(nums)):
            curr += nums[right]
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            if curr == target:
                res = max(res, right - left + 1)

        return res

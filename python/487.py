from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        zeros = 0
        res = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1

        return res

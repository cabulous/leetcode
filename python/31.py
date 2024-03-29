from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]

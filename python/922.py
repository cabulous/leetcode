from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1

        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]

        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = list([None] * n)

        t = 0
        for i, x in enumerate(nums):
            if x % 2 == 0:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(nums):
            if x % 2 == 1:
                ans[t] = x
                t += 2

        return ans

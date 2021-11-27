from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        right_product = 1
        for i in reversed(range(n)):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = down = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                up = down + 1
            elif nums[i - 1] > nums[i]:
                down = up + 1

        return max(up, down)

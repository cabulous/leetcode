from typing import List


# https://leetcode.com/problems/valid-triangle-number/discuss/1339248/Python-sort-%2B-2-pointers-solution-explained
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0

        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1

        return res

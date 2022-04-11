from typing import List


# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/203666/python-sliding-windows-O(n)O(1)
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        window1 = sum(nums[:k])
        window2 = sum(nums[k:2 * k])
        window3 = sum(nums[2 * k:3 * k])

        window1_max = window1
        window2_max = window1 + window2
        window3_max = window1 + window2 + window3

        window1_max_index = [0]
        window2_max_index = [0, k]
        window3_max_index = [0, k, 2 * k]

        for i in range(1, len(nums) - 3 * k + 1):
            window1 += nums[i - 1 + k] - nums[i - 1]
            window2 += nums[i - 1 + 2 * k] - nums[i - 1 + k]
            window3 += nums[i - 1 + 3 * k] - nums[i - 1 + 2 * k]
            if window1 > window1_max:
                window1_max = window1
                window1_max_index = [i]
            if window1_max + window2 > window2_max:
                window2_max = window1_max + window2
                window2_max_index = window1_max_index + [i + k]
            if window2_max + window3 > window3_max:
                window3_max = window2_max + window3
                window3_max_index = window2_max_index + [i + 2 * k]

        return window3_max_index

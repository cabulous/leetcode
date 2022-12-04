from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0

        min_diff = float('inf')
        res = -1

        for i, num in enumerate(nums):
            prefix_sum += num
            left_avg = prefix_sum // (i + 1)
            right_count = len(nums) - 1 - i
            right_avg = (total_sum - prefix_sum) // right_count if right_count != 0 else 0
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                res = i

        return res

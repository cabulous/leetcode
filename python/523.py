from typing import List

# https://leetcode.com/problems/continuous-subarray-sum/solution/1600289
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0: 0}
        total = 0

        for i, num in enumerate(nums):
            total += num
            if total % k not in lookup:
                lookup[total % k] = i + 1
            elif lookup[total % k] < i:
                return True

        return False

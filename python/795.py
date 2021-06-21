from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(upper_bound):
            res = cur = 0
            for n in nums:
                cur = cur + 1 if n <= upper_bound else 0
                res += cur
            return res

        return count(right) - count(left - 1)

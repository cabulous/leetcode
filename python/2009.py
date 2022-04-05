import bisect
from typing import List


# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/discuss/1470853/Python-Binary-Search-Clean-and-Concise
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        nums_count = len(nums)
        res = nums_count

        for i, start_num in enumerate(sorted_nums):
            end_num = start_num + nums_count - 1
            index = bisect.bisect_right(sorted_nums, end_num)
            unique_len = index - i
            res = min(res, nums_count - unique_len)

        return res

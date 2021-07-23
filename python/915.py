from itertools import accumulate
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [None] * n
        min_right = [None] * n

        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num, nums[i])
            max_left[i] = max_num

        min_num = nums[-1]
        for i in reversed(range(n)):
            min_num = min(min_num, nums[i])
            min_right[i] = min_num

        for i in range(1, n):
            if max_left[i - 1] <= min_right[i]:
                return i


# https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/1354458/Python-Two-accumulates-explained
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        t1 = list(accumulate(nums, max))
        t2 = list(accumulate(nums[::-1], min))[::-1]
        for i in range(1, len(nums)):
            if t1[i - 1] <= t2[i]:
                return i

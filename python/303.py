from itertools import accumulate
from typing import List


# https://leetcode.com/problems/range-sum-query-immutable/discuss/75200/A-very-short-Python-solution
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right] - (self.pre_sum[left - 1] if left - 1 >= 0 else 0)

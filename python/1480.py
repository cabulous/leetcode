import itertools
from typing import List


# https://leetcode.com/problems/running-sum-of-1d-array/discuss/691189/JavaC%2B%2BPython-Prefix-Sum
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums))

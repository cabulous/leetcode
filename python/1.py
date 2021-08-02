from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i

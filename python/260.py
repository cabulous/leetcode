from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [x for x in count if count[x] == 1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]

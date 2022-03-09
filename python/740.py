from collections import Counter
from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.points = Counter()

    def deleteAndEarn(self, nums: List[int]) -> int:
        for num in nums:
            self.points[num] += num
        return self.helper(max(nums))

    @lru_cache(None)
    def helper(self, num):
        if num == 0:
            return 0
        if num == 1:
            return self.points[1]
        return max(self.helper(num - 1), self.helper(num - 2) + self.points[num])


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter()
        for num in nums:
            points[num] += num

        two_prev = 0
        one_prev = points[1]

        for num in range(2, max(nums) + 1):
            two_prev, one_prev = one_prev, max(one_prev, two_prev + points[num])

        return one_prev

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.points = Counter()

    def deleteAndEarn(self, nums: List[int]) -> int:
        for num in nums:
            self.points[num] += num

        max_num = max(nums)
        return self.helper(max_num)

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
        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        two_prev = 0
        one_prev = points[1]

        for i in range(2, max_num + 1):
            two_prev, one_prev = one_prev, max(one_prev, two_prev + points[i])

        return one_prev

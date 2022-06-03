from itertools import combinations
from typing import List


# https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]


class Solution:

    def __init__(self):
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.dfs(list(range(1, 10)), k, n, [])
        return self.res

    def dfs(self, nums, count_remain, total_remain, path):
        if count_remain < 0 or total_remain < 0:
            return

        if count_remain == 0 and total_remain == 0:
            self.res.append(path[:])
            return

        for i in range(len(nums)):
            self.dfs(nums[i + 1:], count_remain - 1, total_remain - nums[i], path + [nums[i]])

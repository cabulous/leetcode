from typing import List


# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
class Solution:

    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates, target, [])
        return self.res

    def dfs(self, nums, target, path):
        if target < 0:
            return
        if target == 0:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]])

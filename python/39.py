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


# https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for num in candidates:
            for curr_target in range(num, target + 1):
                if curr_target == num:
                    dp[curr_target].append([num])
                for comb in dp[curr_target - num]:
                    dp[curr_target].append(comb + [num])

        return dp[target]

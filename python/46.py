# https://leetcode.com/problems/permutations/solutions/3850714/100-fast-image-video-explanation-backtracking-c-java-python/
class Solution:

    def __init__(self):
        self.init_val = 11
        self.nums = []
        self.res = []

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.helper(0, [self.init_val] * len(nums))
        return self.res

    def helper(self, idx, curr):
        if idx == len(self.nums):
            self.res.append(list(curr))
            return

        for i in range(len(curr)):
            if curr[i] == self.init_val:
                curr[i] = self.nums[idx]
                self.helper(idx + 1, curr)
                curr[i] = self.init_val

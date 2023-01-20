from typing import List


class Solution:

    def __init__(self):
        self.nums = []
        self.sequence = []
        self.res = set()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack(0)
        return list(self.res)

    def backtrack(self, index):
        if index == len(self.nums):
            if len(self.sequence) >= 2:
                self.res.add(tuple(self.sequence))
            return

        if not self.sequence or self.sequence[-1] <= self.nums[index]:
            self.sequence.append(self.nums[index])
            self.backtrack(index + 1)
            self.sequence.pop()

        self.backtrack(index + 1)

from typing import List


class Solution:

    def __init__(self):
        self.nums = []
        self.curr = []
        self.res = set()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack(0)
        return list(self.res)

    def backtrack(self, index):
        if index == len(self.nums):
            if len(self.curr) >= 2:
                self.res.add(tuple(self.curr))
            return

        if not self.curr or self.curr[-1] <= self.nums[index]:
            self.curr.append(self.nums[index])
            self.backtrack(index + 1)
            self.curr.pop()

        self.backtrack(index + 1)

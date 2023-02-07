class Solution:

    def __init__(self):
        self.nums = []
        self.curr = []
        self.res = set()

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.backtrack(0)
        return list(self.res)

    def backtrack(self, idx):
        if idx == len(self.nums):
            if len(self.curr) >= 2:
                self.res.add(tuple(self.curr))
            return

        if not self.curr or self.curr[-1] <= self.nums[idx]:
            self.curr.append(self.nums[idx])
            self.backtrack(idx + 1)
            self.curr.pop()

        self.backtrack(idx + 1)

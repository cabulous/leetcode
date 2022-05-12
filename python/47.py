from collections import Counter
from typing import List


# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            next_res = []
            for lst in res:
                for i in range(len(lst) + 1):
                    next_res.append(lst[:i] + [num] + lst[i:])
                    if i < len(lst) and lst[i] == num:
                        break
            res = next_res

        return res


class Solution:

    def __init__(self):
        self.nums = []
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack([], Counter(nums))

        return self.res

    def backtrack(self, comb, counter):
        if len(comb) == len(self.nums):
            self.res.append(comb[:])
            return

        for num in counter:
            if counter[num] > 0:
                comb.append(num)
                counter[num] -= 1
                self.backtrack(comb, counter)
                comb.pop()
                counter[num] += 1

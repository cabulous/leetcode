from functools import lru_cache
from typing import List


# https://leetcode.com/problems/pizza-with-3n-slices/discuss/546474/Python-Robber-n3-Houses-in-Cycle
class Solution:

    def __init__(self):
        self.slices = []

    def maxSizeSlices(self, slices: List[int]) -> int:
        self.slices = slices
        return self.dp(0, len(slices) - 1, len(slices) // 3, 1)

    @lru_cache(None)
    def dp(self, start, end, remaining, cycle=0):
        if remaining == 1:
            return max(self.slices[start:end + 1])

        if end - start + 1 < remaining * 2 - 1:
            return -1

        return max(
            self.dp(start + cycle, end - 2, remaining - 1) + self.slices[end],
            self.dp(start, end - 1, remaining),
        )

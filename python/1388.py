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
    def dp(self, i, j, k, cycle=0):
        if k == 1:
            return max(self.slices[i:j + 1])
        if j - i + 1 < k * 2 - 1:
            return -float('inf')
        return max(self.dp(i + cycle, j - 2, k - 1) + self.slices[j], self.dp(i, j - 1, k))

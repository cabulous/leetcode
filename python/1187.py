import bisect
from functools import lru_cache


# https://leetcode.com/problems/make-array-strictly-increasing/solutions/3648097/python-elegant-short-top-down-dp-binary-search/
class Solution:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        self.arr1 = arr1
        self.arr2 = sorted(arr2)

        res = self.dp(0, float('-inf'))

        return res if res != float('inf') else -1

    @lru_cache(None)
    def dp(self, arr1_idx, prev_max):
        if arr1_idx == len(self.arr1):
            return 0

        arr2_idx = bisect.bisect(self.arr2, prev_max)

        return min(
            self.dp(arr1_idx + 1, self.arr1[arr1_idx]) if self.arr1[arr1_idx] > prev_max else float('inf'),
            self.dp(arr1_idx + 1, self.arr2[arr2_idx]) + 1 if arr2_idx < len(self.arr2) else float('inf'),
        )

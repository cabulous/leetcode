# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/solutions/1119801/java-c-python-binary-search/
class Solution:

    def __init__(self):
        self.count = 0
        self.peak_idx = 0

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.count = n
        self.peak_idx = index

        maxSum -= n
        left = 0
        right = maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.calc_sum(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left + 1

    def calc_sum(self, a):
        b = max(0, a - self.peak_idx)
        res = (a + b) * (a - b + 1) // 2
        b = max(0, a - (self.count - 1 - self.peak_idx))
        res += (a + b) * (a - b + 1) // 2
        return res - a

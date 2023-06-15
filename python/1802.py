# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/solutions/1119801/java-c-python-binary-search/
class Solution:

    def __init__(self):
        self.peak_idx = 0
        self.max_idx = 0

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.peak_idx = index
        self.max_idx = n - 1

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

    def calc_sum(self, peak):
        res = 0

        left = max(0, peak - self.peak_idx)
        left_sum = (left + peak) * (peak - left + 1) // 2
        res += left_sum

        right = max(0, peak - (self.max_idx - self.peak_idx))
        right_sum = (peak + right) * (peak - right + 1) // 2
        res += right_sum

        return res - peak

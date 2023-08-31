# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024
class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        dp = [0] + [n + 2] * n

        for i, tap_range in enumerate(ranges):
            left = max(0, i - tap_range) + 1
            right = min(n, i + tap_range) + 1
            for j in range(left, right):
                dp[j] = min(dp[j], dp[max(0, i - tap_range)] + 1)

        return dp[-1] if dp[-1] < n + 2 else -1

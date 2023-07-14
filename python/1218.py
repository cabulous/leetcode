from collections import Counter


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = Counter()
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())

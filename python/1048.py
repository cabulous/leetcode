from typing import List


# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}

        for w in sorted(words, key=len):
            dp[w] = max(1 + dp.get(w[:i] + w[i + 1:], 0) for i in range(len(w)))

        return max(dp.values())

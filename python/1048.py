from collections import Counter


# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        dp = Counter()
        for w in sorted(words, key=len):
            dp[w] = 1 + max(dp[w[:i] + w[i + 1:]] for i in range(len(w)))
        return max(dp.values())

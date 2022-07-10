from collections import defaultdict
from typing import List


# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)

        for w in sorted(words, key=len):
            dp[w] = max(1 + dp[w[:i] + w[i + 1:]] for i in range(len(w)))

        return max(dp.values())

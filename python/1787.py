from collections import defaultdict, Counter
from functools import lru_cache
from typing import List


# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/discuss/1097796/Python-3-Another-short-dp-7-lines-explained
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = 1 << 10

        freq = defaultdict(Counter)
        for i, num in enumerate(nums):
            freq[i % k][num] += 1

        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, n):
            dp[0][i] = -float('inf')

        for i in range(1, k + 1):
            max_row = max(dp[i - 1])
            for j in range(n):
                for mask in freq[i - 1]:
                    dp[i][j] = max(dp[i][j], max_row, dp[i - 1][j ^ mask] + freq[i - 1][mask])

        return len(nums) - dp[-1][0]


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq = [Counter(nums[j] for j in range(i, len(nums), k)) for i in range(k)]
        mxs = [freq[i].most_common(1)[0][1] for i in range(k)]

        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return -10000 * j
            return max(dp(i - 1, j ^ m) + freq[i - 1][m] for m in freq[i - 1])

        return len(nums) - max(sum(mxs) - min(mxs), dp(k, 0))

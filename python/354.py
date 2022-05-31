from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.longest_increasing_seq([x[1] for x in envelopes])

    def longest_increasing_seq(self, nums):
        dp = []

        for num in nums:
            idx = bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num

        return len(dp)

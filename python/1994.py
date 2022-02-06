from collections import Counter
from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/the-number-of-good-subsets/discuss/1444213/Python-DP-solution
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [1] + [0] * (1 << 10)
        count = Counter(nums)

        for n in count:
            if n == 1:
                continue
            if n % 4 == 0 or n % 9 == 0 or n == 25:
                continue
            mask = sum(1 << i for i, p in enumerate(primes) if n % p == 0)
            for i in range(1 << 10):
                if i & mask:
                    continue
                dp[i | mask] = (dp[i | mask] + count[n] * dp[i]) % MOD

        return (1 << count[1]) * (sum(dp) - 1) % MOD

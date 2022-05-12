from itertools import combinations
from typing import List


# https://leetcode.com/problems/parallel-courses-ii/discuss/713978/Python-intuitive-Bit-mask-DP-Explained-BEST
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        reqs = [0] * n
        for u, v in relations:
            reqs[v - 1] |= 1 << (u - 1)

        dp = [n] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            available = []

            for v in range(n):
                if mask & (1 << v) == 0 and mask & reqs[v] == reqs[v]:
                    available.append(v)

            for choice in combinations(available, min(k, len(available))):
                mask2 = mask
                for u in choice:
                    mask2 |= (1 << u)
                dp[mask2] = min(dp[mask2], 1 + dp[mask])

        return dp[-1]

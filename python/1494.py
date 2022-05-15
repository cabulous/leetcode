from itertools import combinations
from typing import List


# https://leetcode.com/problems/parallel-courses-ii/discuss/713978/Python-intuitive-Bit-mask-DP-Explained-BEST
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        reqs = [0] * n
        for pre, nxt in relations:
            reqs[nxt - 1] |= 1 << (pre - 1)

        dp = [n] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            available = []
            for course in range(n):
                if mask & (1 << course) == 0 and mask & reqs[course] == reqs[course]:
                    available.append(course)

            for choice in combinations(available, min(k, len(available))):
                next_mask = mask
                for course in choice:
                    next_mask |= (1 << course)
                dp[next_mask] = min(dp[next_mask], 1 + dp[mask])

        return dp[-1]

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        projects = sorted(zip(capital, profits), key=lambda x: -x[0])
        candidates = []
        taken_count = 0
        res = w

        while taken_count < k:
            while projects and projects[-1][0] <= res:
                heapq.heappush(candidates, -projects.pop()[1])
            if not candidates:
                return res
            res += -heapq.heappop(candidates)
            taken_count += 1

        return res

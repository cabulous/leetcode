import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort(key=lambda x: -x[0])

        taken = []
        res = w
        while k > 0:
            while projects and projects[-1][0] <= res:
                heapq.heappush(taken, -projects.pop()[1])
            if taken:
                res -= heapq.heappop(taken)
            else:
                break
            k -= 1

        return res

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        projects = sorted(list(zip(capital, profits)), key=lambda x: -x[0])
        projects_taken = []
        projects_count = 0
        res = w

        while projects_count < k:
            while projects and projects[-1][0] <= res:
                heapq.heappush(projects_taken, -projects.pop()[1])
            if len(projects_taken) > 0:
                max_profit = -heapq.heappop(projects_taken)
                res += max_profit
            else:
                break
            projects_count += 1

        return res

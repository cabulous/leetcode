from typing import List


# https://leetcode.com/problems/maximum-vacation-days/discuss/102680/Python-Simple-with-Explanation
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n_inf = float('-inf')
        n, k = len(days), len(days[0])
        best = [n_inf] * n
        best[0] = 0

        for week in range(k):
            curr = [n_inf] * n
            for city_i in range(n):
                for city_j, adj in enumerate(flights[city_i]):
                    if adj or city_i == city_j:
                        curr[city_j] = max(curr[city_j], best[city_i] + days[city_j][week])
            best = curr

        return int(max(best))

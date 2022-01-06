from typing import List


# https://leetcode.com/problems/maximum-vacation-days/discuss/102680/Python-Simple-with-Explanation
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        city_count, week_count = len(days), len(days[0])
        best = [float('-inf')] * city_count
        best[0] = 0

        for week in range(week_count):
            curr_best = [float('-inf')] * city_count
            for city in range(city_count):
                for next_city, adj in enumerate(flights[city]):
                    if adj or city == next_city:
                        curr_best[next_city] = max(curr_best[next_city], best[city] + days[next_city][week])
            best = curr_best

        return int(max(best))

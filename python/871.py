import heapq
from typing import List


# heap
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append([target, float('inf')])
        tank = startFuel
        prev_location = 0
        steps = 0

        for location, capacity in stations:
            tank -= (location - prev_location)
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                steps += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev_location = location

        return steps


# dp
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)

        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1

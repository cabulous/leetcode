import heapq
import math
from typing import List


# heap
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, math.inf])

        max_heap = []
        tank = startFuel
        prev_location = 0
        res = 0

        for location, capacity in stations:
            tank -= location - prev_location
            while tank < 0 and max_heap:
                tank += -heapq.heappop(max_heap)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(max_heap, -capacity)
            prev_location = location

        return res


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

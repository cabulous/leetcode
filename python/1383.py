import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7

        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key=lambda t: t[0], reverse=True)

        speed_heap = []
        speed_sum = 0
        perf = 0
        for curr_efficiency, curr_speed in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)

        return perf % modulo

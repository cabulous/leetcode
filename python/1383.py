import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7

        candidates = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)

        speed_min_heap = []
        speed_sum = 0
        res = 0

        for curr_efficiency, curr_speed in candidates:
            while len(speed_min_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_min_heap)
            heapq.heappush(speed_min_heap, curr_speed)
            speed_sum += curr_speed
            res = max(res, speed_sum * curr_efficiency)

        return res % modulo

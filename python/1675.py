import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        num_min = float('inf')

        for num in nums:
            if num % 2 == 0:
                heapq.heappush(max_heap, -num)
                num_min = min(num_min, num)
            else:
                heapq.heappush(max_heap, -num * 2)
                num_min = min(num_min, num * 2)

        res = float('inf')

        while max_heap:
            num_max = -heapq.heappop(max_heap)
            res = min(res, num_max - num_min)
            if num_max % 2 == 1:
                return res
            heapq.heappush(max_heap, -num_max // 2)
            num_min = min(num_min, num_max // 2)

        return res

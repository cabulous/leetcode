import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        num_min = float('inf')

        for num in nums:
            if num % 2 == 0:
                heapq.heappush(evens, -num)
                num_min = min(num_min, num)
            else:
                heapq.heappush(evens, -num * 2)
                num_min = min(num_min, num * 2)

        res = float('inf')

        while evens:
            num_max = -heapq.heappop(evens)
            res = min(res, num_max - num_min)
            if num_max % 2 == 1:
                return res
            heapq.heappush(evens, -num_max // 2)
            num_min = min(num_min, num_max // 2)

        return res

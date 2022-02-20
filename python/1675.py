import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        num_min = float('inf')

        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                num_min = min(num_min, num)
            else:
                evens.append(-num * 2)
                num_min = min(num_min, num * 2)

        heapq.heapify(evens)
        res = float('inf')

        while evens:
            num_max = -heapq.heappop(evens)
            res = min(res, num_max - num_min)
            if num_max % 2 == 0:
                num_min = min(num_min, num_max // 2)
                heapq.heappush(evens, -num_max // 2)
            else:
                return res

        return res

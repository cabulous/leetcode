import heapq
from math import inf
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = inf

        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num * 2)
                minimum = min(minimum, num * 2)

        heapq.heapify(evens)
        min_deviation = inf

        while evens:
            maximum = -heapq.heappop(evens)
            min_deviation = min(min_deviation, maximum - minimum)
            if maximum % 2 == 0:
                minimum = min(minimum, maximum // 2)
                heapq.heappush(evens, -maximum // 2)
            else:
                break

        return min_deviation

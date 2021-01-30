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
            curr_value = -heapq.heappop(evens)
            min_deviation = min(min_deviation, curr_value - minimum)
            if curr_value % 2 == 0:
                minimum = min(minimum, curr_value // 2)
                heapq.heappush(evens, -curr_value // 2)
            else:
                break

        return min_deviation

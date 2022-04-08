import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = nums[:]
        heapq.heapify(self.queue)
        while len(self.queue) > k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        if len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]

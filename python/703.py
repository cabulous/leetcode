import heapq


# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heappushpop(self.pool, val)
        return self.pool[0]

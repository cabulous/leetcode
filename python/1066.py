import heapq
from typing import List


# https://leetcode.com/problems/campus-bikes-ii/discuss/303422/Python-Priority-Queue
class Solution:
    def __init__(self):
        self.workers = []
        self.bikes = []

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.workers, self.bikes = workers, bikes
        queue = [[0, 0, 0]]
        seen = set()

        while True:
            cost, i, taken = heapq.heappop(queue)
            if (i, taken) in seen:
                continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(queue, [cost + self.manhattan_dist(i, j), i + 1, taken | (1 << j)])

    def manhattan_dist(self, i, j):
        return abs(self.workers[i][0] - self.bikes[j][0]) + abs(self.workers[i][1] - self.bikes[j][1])

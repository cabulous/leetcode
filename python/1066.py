import heapq
from typing import List


class Solution:

    def __init__(self):
        self.workers = []
        self.bikes = []

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.workers = workers
        self.bikes = bikes

        queue = [(0, 0, 0)]
        seen = set()

        while queue:
            cost, worker_idx, bike_taken = heapq.heappop(queue)
            if worker_idx == len(workers):
                return cost
            if (worker_idx, bike_taken) in seen:
                continue
            seen.add((worker_idx, bike_taken))
            for bike_idx in range(len(bikes)):
                if bike_taken & (1 << bike_idx) == 0:
                    next_cost = cost + self.manhattan_dist(worker_idx, bike_idx)
                    next_bike_taken = bike_taken | (1 << bike_idx)
                    heapq.heappush(queue, (next_cost, worker_idx + 1, next_bike_taken))

        return -1

    def manhattan_dist(self, worker_idx, bike_idx):
        worker_x, worker_y = self.workers[worker_idx]
        bike_x, bike_y = self.bikes[bike_idx]
        return abs(worker_x - bike_x) + abs(worker_y - bike_y)

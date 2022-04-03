import heapq
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        worker_to_bike_group = []
        queue = []

        for worker, worker_loc in enumerate(workers):
            curr = []
            for bike, bike_loc in enumerate(bikes):
                distance = self.get_distance(worker_loc, bike_loc)
                curr.append((distance, worker, bike))
            curr.sort(reverse=True)
            heapq.heappush(queue, curr.pop())
            worker_to_bike_group.append(curr)

        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)

        while queue:
            distance, worker, bike = heapq.heappop(queue)
            if not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
            else:
                next_closest_bike = worker_to_bike_group[worker].pop()
                heapq.heappush(queue, next_closest_bike)

        return worker_status

    def get_distance(self, worker_loc, bike_loc):
        return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])

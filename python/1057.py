import heapq
from collections import defaultdict
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        worker_to_bike_group = []
        queue = []

        for worker, worker_loc in enumerate(workers):
            curr_worker_pairs = []
            for bike, bike_loc in enumerate(bikes):
                distance = self.get_distance(worker_loc, bike_loc)
                curr_worker_pairs.append((distance, worker, bike))
            curr_worker_pairs.sort(reverse=True)
            heapq.heappush(queue, curr_worker_pairs.pop())
            worker_to_bike_group.append(curr_worker_pairs)

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


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        all_triplets = []
        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = self.get_distance(worker_loc, bike_loc)
                all_triplets.append((distance, worker, bike))

        all_triplets.sort()

        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
        pair_count = 0

        for distance, worker, bike in all_triplets:
            if worker_status[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1
                if pair_count == len(workers):
                    return worker_status

        return worker_status

    def get_distance(self, worker_loc, bike_loc):
        return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        min_dist = float('inf')
        dist_to_pairs = defaultdict(list)

        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = self.get_distance(worker_loc, bike_loc)
                dist_to_pairs[distance].append((worker, bike))
                min_dist = min(min_dist, distance)

        curr_dist = min_dist
        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
        pair_count = 0

        while pair_count < len(workers):
            for worker, bike in dist_to_pairs[curr_dist]:
                if worker_status[worker] == -1 and not bike_status[bike]:
                    bike_status[bike] = True
                    worker_status[worker] = bike
                    pair_count += 1
            curr_dist += 1

        return worker_status

    def get_distance(self, worker_loc, bike_loc):
        return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])

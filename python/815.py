from collections import defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        to_routes = defaultdict(set)

        for bus_idx, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(bus_idx)

        queue = [(source, 0)]
        seen = {source}

        for stop, count in queue:
            if stop == target:
                return count
            for bus_idx in to_routes[stop]:
                for next_stop in routes[bus_idx]:
                    if next_stop not in seen:
                        seen.add(next_stop)
                        queue.append((next_stop, count + 1))
                routes[bus_idx] = []

        return -1

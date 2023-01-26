import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        queue = [(0, src, 0)]
        dist = [[float('inf')] * (k + 2) for _ in range(n)]

        while queue:
            cost, node, steps = heapq.heappop(queue)
            if node == dst:
                return cost
            if steps > k:
                continue
            for next_node, next_cost in graph[node]:
                next_dist = cost + next_cost
                if next_dist < dist[next_node][steps + 1]:
                    dist[next_node][steps + 1] = next_dist
                    heapq.heappush(queue, (next_dist, next_node, steps + 1))

        return -1

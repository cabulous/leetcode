import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))

        queue = [(0, src, 0)]
        min_cost = [[float('inf')] * (k + 2) for _ in range(n)]

        while queue:
            cost, node, steps = heapq.heappop(queue)
            if node == dst:
                return cost
            if steps > k:
                continue
            for next_node, next_price in graph[node]:
                next_cost = cost + next_price
                next_step = steps + 1
                if next_cost < min_cost[next_node][next_step]:
                    min_cost[next_node][next_step] = next_cost
                    heapq.heappush(queue, (next_cost, next_node, next_step))

        return -1

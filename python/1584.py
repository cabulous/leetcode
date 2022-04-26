import math
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        edges_used = 0
        in_mst = [False] * n

        min_dist = [math.inf] * n
        min_dist[0] = 0

        while edges_used < n:
            curr_min_edge = math.inf
            curr_node = -1

            for node in range(n):
                if not in_mst[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr_node = node

            res += curr_min_edge
            edges_used += 1
            in_mst[curr_node] = True

            for next_node in range(n):
                weight = self.get_manhattan_dist(points[curr_node], points[next_node])
                if not in_mst[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight

        return res

    def get_manhattan_dist(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

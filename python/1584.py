import math
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges_used = 0
        res = 0

        visited = [False] * n
        min_dist = [math.inf] * n
        min_dist[0] = 0

        while edges_used < n:
            curr_min_dist = math.inf
            curr_node = -1

            for node in range(n):
                if not visited[node] and min_dist[node] < curr_min_dist:
                    curr_min_dist = min_dist[node]
                    curr_node = node

            res += curr_min_dist
            edges_used += 1
            visited[curr_node] = True

            for next_node in range(n):
                dist = self.get_manhattan_dist(points[curr_node], points[next_node])
                if not visited[next_node] and dist < min_dist[next_node]:
                    min_dist[next_node] = dist

        return res

    def get_manhattan_dist(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

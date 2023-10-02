class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        visited = [False] * len(points)
        min_dist = [float('inf')] * len(points)
        min_dist[0] = 0
        used = 0
        res = 0

        while used < len(points):
            curr_min_dist = float('inf')
            curr_node = -1
            for node in range(len(points)):
                if not visited[node] and min_dist[node] < curr_min_dist:
                    curr_min_dist = min_dist[node]
                    curr_node = node

            visited[curr_node] = True
            used += 1
            res += curr_min_dist

            x1, y1 = points[curr_node]
            for next_node in range(len(points)):
                if not visited[next_node]:
                    x2, y2 = points[next_node]
                    next_dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[next_node] = min(min_dist[next_node], next_dist)

        return res

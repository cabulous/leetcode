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

            for next_node in range(len(points)):
                next_dist = self.get_dist(points[curr_node], points[next_node])
                if not visited[next_node] and next_dist < min_dist[next_node]:
                    min_dist[next_node] = next_dist

        return res

    def get_dist(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

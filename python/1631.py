import heapq


# Dijkstra's Algorithm
# https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Clean-and-Concise-O(MNlogMN)
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        min_dist = [[float('inf')] * cols for _ in range(rows)]
        queue = [(0, 0, 0)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            dist, row, col = heapq.heappop(queue)
            if (row, col) == (rows - 1, cols - 1):
                return dist
            if dist > min_dist[row][col]:
                continue
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nd = max(dist, abs(heights[nr][nc] - heights[row][col]))
                    if nd < min_dist[nr][nc]:
                        min_dist[nr][nc] = nd
                        heapq.heappush(queue, (nd, nr, nc))

        return -1

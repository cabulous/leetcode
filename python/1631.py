import heapq
import math
from typing import List


# bfs
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        max_row, max_col = len(heights), len(heights[0])

        def can_reach_destination(mid: int) -> bool:
            visited = [[False] * max_col for _ in range(max_row)]
            queue = [(0, 0)]
            while queue:
                x, y = queue.pop()
                if x == max_row - 1 and y == max_col - 1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < max_row and 0 <= ny < max_col and not visited[nx][ny]:
                        curr_diff = abs(heights[nx][ny] - heights[x][y])
                        if curr_diff <= mid:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return False

        left, right = 0, 1_000_000
        while left <= right:
            mid = left + (right - left) // 2
            if can_reach_destination(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# Dijkstra's Algorithm
# https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Clean-and-Concise-O(MNlogMN)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        min_heap = [(0, 0, 0)]
        direction = [0, 1, 0, -1, 0]
        while min_heap:
            distance, r, c = heapq.heappop(min_heap)
            if distance > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return distance
            for i in range(4):
                nr, nc = r + direction[i], c + direction[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    new_distance = max(distance, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > new_distance:
                        dist[nr][nc] = new_distance
                        heapq.heappush(min_heap, (dist[nr][nc], nr, nc))
        return 0

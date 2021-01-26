import heapq
import math
from typing import List


# bfs
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])

        def can_reach_destination(mid):
            visited = [[False] * col for _ in range(row)]
            queue = [(0, 0)]
            while queue:
                x, y = queue.pop()
                if x == row - 1 and y == col - 1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                        curr_diff = abs(heights[nx][ny] - heights[x][y])
                        if curr_diff <= mid:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

        left, right = 0, 10000000
        while left <= right:
            mid = left + (right - left) // 2
            if can_reach_destination(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# Dijkstra's Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        diff_matrix = [[math.inf] * col for _ in range(row)]
        diff_matrix[0][0] = 0
        visited = [[False] * col for _ in range(row)]
        queue = [(0, 0, 0)]
        while queue:
            diff, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    curr_diff = abs(heights[nx][ny] - heights[x][y])
                    max_diff = max(curr_diff, int(diff_matrix[x][y]))
                    if diff_matrix[nx][ny] > max_diff:
                        diff_matrix[nx][ny] = max_diff
                        heapq.heappush(queue, (max_diff, nx, ny))
        return int(diff_matrix[-1][-1])

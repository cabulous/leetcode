import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while pq:
            elevation, row, col = heapq.heappop(pq)
            res = max(res, elevation)
            if row == col == n - 1:
                return res
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))


# https://leetcode.com/problems/swim-in-rising-water/discuss/113765/PythonC%2B%2B-Binary-Search
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = grid[0][0], n * n - 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def reachable(time):
            bfs = [(0, 0)]
            seen = {(0, 0)}
            for row, col in bfs:
                if grid[row][col] <= time:
                    if row == col == n - 1:
                        return True
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            bfs.append((nr, nc))
            return False

        while left < right:
            mid = left + (right - left) // 2
            if reachable(mid):
                right = mid
            else:
                left = mid + 1

        return right

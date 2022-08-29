import heapq
from typing import List


# https://leetcode.com/problems/the-maze-ii/discuss/150536/Python-simple-and-elegant-PriorityQueue-solution-beats-97
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = [(0, start[0], start[1])]
        stopped = {(start[0], start[1]): 0}

        while queue:
            dist, r, c = heapq.heappop(queue)
            if [r, c] == destination:
                return dist

            for dr, dc in directions:
                nd, nr, nc = dist, r, c
                while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                    nd += 1
                    nr += dr
                    nc += dc
                if (nr, nc) not in stopped or nd < stopped[nr, nc]:
                    stopped[nr, nc] = nd
                    heapq.heappush(queue, (nd, nr, nc))

        return -1

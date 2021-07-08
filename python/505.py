import heapq
from typing import List


# https://leetcode.com/problems/the-maze-ii/discuss/150536/Python-simple-and-elegant-PriorityQueue-solution-beats-97
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        max_row, max_col = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])]
        stopped = {(start[0], start[1]): 0}
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            dist, row, col = heapq.heappop(queue)
            if [row, col] == destination:
                return dist
            for dr, dc in directions:
                nd, nr, nc = dist, row, col
                while 0 <= nr + dr < max_row and 0 <= nc + dc < max_col and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    nd += 1
                if (nr, nc) not in stopped or nd < stopped[(nr, nc)]:
                    stopped[(nr, nc)] = nd
                    heapq.heappush(queue, (nd, nr, nc))

        return -1

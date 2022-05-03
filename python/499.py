import heapq
from typing import List


# https://leetcode.com/problems/the-maze-iii/discuss/150550/Python-Short-PriorityQueue-solution-beats-100
class Solution:

    def __init__(self):
        self.maze = []
        self.rows = 0
        self.cols = 0
        self.hole = []

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        self.maze = maze
        self.rows, self.cols = len(maze), len(maze[0])
        self.hole = hole

        queue = [(0, '', ball[0], ball[1])]
        stopped = {(ball[0], ball[1]): [0, '']}

        while queue:
            dist, pattern, row, col = heapq.heappop(queue)

            if [row, col] == hole:
                return pattern

            for next_row, next_col, delta_pattern, delta_dist in self.get_next_step(row, col):
                next_pattern = pattern + delta_pattern
                next_dist = dist + delta_dist
                if (next_row, next_col) in stopped and stopped[next_row, next_col] <= [next_dist, next_pattern]:
                    continue
                stopped[next_row, next_col] = [next_dist, next_pattern]
                heapq.heappush(queue, (next_dist, next_pattern, next_row, next_col))

        return 'impossible'

    def get_next_step(self, row, col):
        for dr, dc, pattern in ((-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')):
            nr, nc, dist = row, col, 0
            while 0 <= nr + dr < self.rows and 0 <= nc + dc < self.cols and self.maze[nr + dr][nc + dc] != 1:
                nr += dr
                nc += dc
                dist += 1
                if [nr, nc] == self.hole:
                    break
            yield nr, nc, pattern, dist

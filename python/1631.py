import heapq
import math
from typing import List


# Dijkstra's Algorithm
# https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Clean-and-Concise-O(MNlogMN)
class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])
        dist_matrix = [[math.inf] * self.cols for _ in range(self.rows)]
        queue = [(0, 0, 0)]

        while queue:
            dist, row, col = heapq.heappop(queue)
            if dist > dist_matrix[row][col]:
                continue
            if (row, col) == (self.rows - 1, self.cols - 1):
                return dist
            for next_row, next_col in self.get_next_cell(row, col):
                next_dist = max(dist, abs(heights[next_row][next_col] - heights[row][col]))
                if next_dist < dist_matrix[next_row][next_col]:
                    dist_matrix[next_row][next_col] = next_dist
                    heapq.heappush(queue, (next_dist, next_row, next_col))

    def get_next_cell(self, row, col):
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                yield next_row, next_col

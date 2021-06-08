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
                new_row, new_col = row, col
                curr_dist = 0
                while 0 <= new_row + dr < max_row and 0 <= new_col + dc < max_col and maze[new_row + dr][
                    new_col + dc] == 0:
                    new_row += dr
                    new_col += dc
                    curr_dist += 1
                new_dist = dist + curr_dist
                if (new_row, new_col) not in stopped or new_dist < stopped[(new_row, new_col)]:
                    stopped[(new_row, new_col)] = new_dist
                    heapq.heappush(queue, (new_dist, new_row, new_col))

        return -1

from collections import deque
from typing import List


# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/693918/Python-BFS-*-BFS-or-130ms-or-beats-95-or-Explained-and-Commented
class Solution:

    def __init__(self):
        self.grid = []

    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        rows, cols = len(grid), len(grid[0])
        target = box = person = None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'T':
                    target = (r, c)
                elif grid[r][c] == 'B':
                    box = (r, c)
                elif grid[r][c] == 'S':
                    person = (r, c)

        queue = deque([(0, box, person)])
        visited = {box + person}

        while queue:
            distance, box, person = queue.popleft()
            if box == target:
                return distance

            box_row, box_col = box

            box_coordinate = [(box_row + 1, box_col), (box_row - 1, box_col), (box_row, box_col + 1),
                              (box_row, box_col - 1)]
            person_coordinate = [(box_row - 1, box_col), (box_row + 1, box_col), (box_row, box_col - 1),
                                 (box_row, box_col + 1)]

            for new_box, new_person in zip(box_coordinate, person_coordinate):
                if self.valid(*new_box) and new_box + box not in visited:
                    if self.valid(*new_person) and self.check(person, new_person, box):
                        visited.add(new_box + box)
                        queue.append((distance + 1, new_box, box))

        return -1

    def valid(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] != '#'

    def check(self, curr, destination, box):
        queue = deque([curr])
        seen = set()
        while queue:
            row, col = queue.popleft()
            if (row, col) == destination:
                return True
            for next_row, next_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if not self.valid(next_row, next_col):
                    continue
                if (next_row, next_col) in seen:
                    continue
                if (next_row, next_col) == box:
                    continue
                seen.add((next_row, next_col))
                queue.append((next_row, next_col))
        return False

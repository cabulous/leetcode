import copy
from typing import List


# https://leetcode.com/problems/contain-virus/discuss/138423/python-solution-(BFS-112ms)
class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.grid = []

    def containVirus(self, isInfected: List[List[int]]) -> int:
        self.rows, self.cols = len(isInfected), len(isInfected[0])
        self.grid = copy.deepcopy(isInfected)

        virus_areas, dangers, walls = self.get_areas()
        wall_count = 0

        while virus_areas:
            if sum(len(area) for area in virus_areas) == self.rows * self.cols:
                return wall_count

            most_danger_index = 0
            for i, danger in enumerate(dangers):
                if len(danger) > len(dangers[most_danger_index]):
                    most_danger_index = i

            wall_count += walls[most_danger_index]
            for r, c in virus_areas[most_danger_index]:
                self.grid[r][c] = -1

            self.spread(dangers[:most_danger_index] + dangers[most_danger_index + 1:])

            virus_areas, dangers, walls = self.get_areas()

        return wall_count

    def get_adj(self, row, col):
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                yield next_row, next_col

    def spread(self, dangers):
        for danger in dangers:
            for row, col in danger:
                self.grid[row][col] = 1

    def get_areas(self):
        virus_areas = []
        dangers = []
        walls = []
        seen = [[False] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and not seen[r][c]:
                    seen[r][c] = True
                    area = [(r, c)]
                    danger = set()
                    wall = 0
                    queue = [(r, c)]
                    while queue:
                        curr_r, curr_c = queue.pop()
                        for next_r, next_c in self.get_adj(curr_r, curr_c):
                            if self.grid[next_r][next_c] == 1 and not seen[next_r][next_c]:
                                seen[next_r][next_c] = True
                                area.append((next_r, next_c))
                                queue.append((next_r, next_c))
                            elif self.grid[next_r][next_c] == 0:
                                danger.add((next_r, next_c))
                                wall += 1
                    virus_areas.append(area)
                    dangers.append(danger)
                    walls.append(wall)

        return virus_areas, dangers, walls

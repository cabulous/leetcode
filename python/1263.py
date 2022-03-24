from collections import deque
from typing import List


# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/693918/Python-BFS-*-BFS-or-130ms-or-beats-95-or-Explained-and-Commented
class Solution:

    def __init__(self):
        self.grid = []

    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid

        destination = None
        box_position = None
        person_position = None

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'T':
                    destination = (row, col)
                elif grid[row][col] == 'B':
                    box_position = (row, col)
                elif grid[row][col] == 'S':
                    person_position = (row, col)

        queue = deque([(0, box_position, person_position)])
        visited = {box_position + person_position}

        while queue:
            distance, box, person = queue.popleft()
            if box == destination:
                return distance

            box_row, box_col = box
            box_coordinates = [(box_row + 1, box_col), (box_row - 1, box_col), (box_row, box_col + 1),
                               (box_row, box_col - 1)]
            person_coordinates = [(box_row - 1, box_col), (box_row + 1, box_col), (box_row, box_col - 1),
                                  (box_row, box_col + 1)]

            for next_box, next_person in zip(box_coordinates, person_coordinates):
                if self.is_valid(*next_box) and next_box + box not in visited:
                    if self.is_valid(*next_person) and self.check(person, next_person, box):
                        visited.add(next_box + box)
                        queue.append((distance + 1, next_box, box))

        return -1

    def is_valid(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] != '#'

    def check(self, curr_position, destination, box_position):
        queue = deque([curr_position])
        visited = set()

        while queue:
            position = queue.popleft()
            if position == destination:
                return True

            row, col = position
            for next_row, next_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if not self.is_valid(next_row, next_col):
                    continue
                if (next_row, next_col) in visited:
                    continue
                if (next_row, next_col) == box_position:
                    continue
                visited.add((next_row, next_col))
                queue.append((next_row, next_col))

        return False

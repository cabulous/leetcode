from functools import lru_cache
from typing import List


# https://leetcode.com/problems/maximum-students-taking-exam/discuss/503433/Python-DFS-with-memorization
class Solution:

    def __init__(self):
        self.seats = []
        self.rows = 0
        self.cols = 0

    def maxStudents(self, seats: List[List[str]]) -> int:
        self.seats = seats
        self.rows = len(seats)
        self.cols = len(seats[0])

        return self.solve(0, 0, 0)

    def get_next_seat(self, row, col):
        return (row, col + 1) if col < self.cols - 1 else (row + 1, 0)

    def transform(self, mask):
        res = 0
        for i in range(self.cols, 2 * self.cols):
            if mask & 1 << i != 0:
                res |= 1 << (i - self.cols)
        return res

    @lru_cache(None)
    def solve(self, row, col, mask):
        if row == self.rows:
            return 0

        if col == 0:
            mask = self.transform(mask)

        next_row, next_col = self.get_next_seat(row, col)
        res = self.solve(next_row, next_col, mask)

        if self.seats[row][col] == '#':
            return res

        for dr, dc in [(0, -1), (-1, 1), (-1, -1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and mask & 1 << ((nr == row) * self.cols + nc):
                break
        else:
            res = max(res, self.solve(next_row, next_col, mask | 1 << (self.cols + col)) + 1)

        return res

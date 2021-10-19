from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.dp = []

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.rows, self.cols = len(dungeon), len(dungeon[0])
        self.dp = [[float('inf')] * self.cols for _ in range(self.rows)]

        for row in reversed(range(self.rows)):
            for col in reversed(range(self.cols)):
                cur_cell = dungeon[row][col]
                right_health = self.get_min_health(cur_cell, row, col + 1)
                down_health = self.get_min_health(cur_cell, row + 1, col)
                next_health = min(right_health, down_health)
                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if cur_cell >= 0 else 1 - cur_cell
                self.dp[row][col] = min_health

        return int(self.dp[0][0])

    def get_min_health(self, cur_cell, next_row, next_col):
        if next_row >= self.rows or next_col >= self.cols:
            return float('inf')
        next_cell = self.dp[next_row][next_col]
        return max(1, next_cell - cur_cell)

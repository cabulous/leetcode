from typing import List


# https://leetcode.com/problems/where-will-the-ball-fall/discuss/988576/JavaC%2B%2BPython-Solution-with-Explanation
class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        return list(map(self.helper, range(self.cols)))

    def helper(self, col):
        curr_col = col
        for row in range(self.rows):
            next_col = curr_col + self.grid[row][curr_col]
            if next_col < 0 or self.cols <= next_col or self.grid[row][curr_col] != self.grid[row][next_col]:
                return -1
            curr_col = next_col
        return curr_col

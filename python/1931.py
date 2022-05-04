from functools import lru_cache

MOD = 1_000_000_007


# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/discuss/1330185/C%2B%2BPython-DP-and-DFS-and-Bitmask-Picture-explain-Clean-and-Concise
class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def colorTheGrid(self, m: int, n: int) -> int:
        self.rows = m
        self.cols = n

        return self.dp(0, 0)

    def get_color(self, mask, pos):
        return (mask >> (2 * pos)) & 3

    def set_color(self, mask, pos, color):
        return mask | (color << (2 * pos))

    def dfs(self, row, curr_col_mask, prev_col_mask, out):
        if row == self.rows:
            out.append(curr_col_mask)
            return
        for color in [1, 2, 3]:
            diff_from_left = self.get_color(prev_col_mask, row) != color
            diff_from_top = self.get_color(curr_col_mask, row - 1) != color
            if diff_from_left and (row != 0 or diff_from_top):
                self.dfs(row + 1, self.set_color(curr_col_mask, row, color), prev_col_mask, out)

    @lru_cache(None)
    def neighbor(self, prev_col_mask):
        out = []
        self.dfs(0, 0, prev_col_mask, out)
        return out

    @lru_cache(None)
    def dp(self, col, prev_col_mask):
        if col == self.cols:
            return 1

        res = 0

        for nei in self.neighbor(prev_col_mask):
            res = (res + self.dp(col + 1, nei)) % MOD

        return res

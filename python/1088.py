# https://leetcode.com/problems/confusing-number-ii/discuss/1365889/Python-Backtracking-Solution-Clear-explanation-Clean-and-Concise
class Solution:

    def __init__(self):
        self.res = 0
        self.rotate180 = [[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]
        self.num_max = 0

    def confusingNumberII(self, n: int) -> int:
        self.num_max = n
        self.dfs(0, 0, 1)
        return self.res

    def dfs(self, num, num_rotated, unit):
        if num != num_rotated:
            self.res += 1

        for d, d_rotated in self.rotate180:
            if d == 0 and num == 0:
                continue
            if num * 10 + d > self.num_max:
                break
            self.dfs(num * 10 + d, num_rotated * unit + d_rotated, unit * 10)

# https://leetcode.com/problems/confusing-number-ii/discuss/1365889/Python-Backtracking-Solution-Clear-explanation-Clean-and-Concise
class Solution:

    def __init__(self):
        self.rotate180 = [[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]
        self.num_max = 0
        self.res = 0

    def confusingNumberII(self, n: int) -> int:
        self.num_max = n
        self.dfs(0, 0, 1)
        return self.res

    def dfs(self, num, num_rotated, unit_rotated):
        if num != num_rotated:
            self.res += 1

        for digit, digit_rotated in self.rotate180:
            if digit == num == 0:
                continue
            if num * 10 + digit > self.num_max:
                break
            self.dfs(
                num * 10 + digit,
                digit_rotated * unit_rotated + num_rotated,
                unit_rotated * 10,
            )

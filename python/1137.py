from functools import lru_cache


class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z

        return z


class Tri:
    def __init__(self):
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]


class Solution:
    t = Tri()

    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]

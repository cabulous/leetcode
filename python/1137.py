from functools import lru_cache


class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n > 0 else 0
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n > 0 else 0

        x, y, z = 0, 1, 1
        for __ in range(n - 2):
            x, y, z = y, z, x + y + z

        return z

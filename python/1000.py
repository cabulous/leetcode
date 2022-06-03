from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.k = 0
        self.prefix = []

    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        self.k = k
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + stones[i]

        return self.dp(0, n - 1)

    @lru_cache(None)
    def dp(self, i, j):
        if j - i + 1 < self.k:
            return 0

        res = min(self.dp(i, mid) + self.dp(mid + 1, j) for mid in range(i, j, self.k - 1))

        if (j - i) % (self.k - 1) == 0:
            res += self.prefix[j + 1] - self.prefix[i]

        return res

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
    def dp(self, left, right):
        if right - left + 1 < self.k:
            return 0

        res = min(self.dp(left, mid) + self.dp(mid + 1, right) for mid in range(left, right, self.k - 1))

        if (right - left) % (self.k - 1) == 0:
            res += self.prefix[right + 1] - self.prefix[left]

        return res

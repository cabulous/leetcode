from functools import lru_cache


class Solution:

    def __init__(self):
        self.events = []

    def maxValue(self, events: list[list[int]], k: int) -> int:
        self.events = sorted(events)
        return self.dp(0, k, 0)

    @lru_cache(None)
    def dp(self, idx, remain, prev_end):
        if remain == 0 or idx == len(self.events):
            return 0

        start, end, val = self.events[idx]
        if start <= prev_end:
            return self.dp(idx + 1, remain, prev_end)

        attend = val + self.dp(idx + 1, remain - 1, end)
        skip = self.dp(idx + 1, remain, prev_end)

        return max(attend, skip)

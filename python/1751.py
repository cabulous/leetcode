class Solution:

    def __init__(self):
        self.events = []
        self.memo = {}

    def maxValue(self, events: list[list[int]], k: int) -> int:
        self.events = sorted(events)
        return self.dp(0, k, 0)

    def dp(self, idx, remain, prev_end):
        if remain == 0:
            return 0

        if idx == len(self.events):
            return 0

        if (idx, remain, prev_end) in self.memo:
            return self.memo[idx, remain, prev_end]

        start, end, val = self.events[idx]
        if start <= prev_end:
            self.memo[idx, remain, prev_end] = self.dp(idx + 1, remain, prev_end)
            return self.memo[idx, remain, prev_end]

        attend = val + self.dp(idx + 1, remain - 1, end)
        skip = self.dp(idx + 1, remain, prev_end)
        self.memo[idx, remain, prev_end] = max(attend, skip)

        return self.memo[idx, remain, prev_end]

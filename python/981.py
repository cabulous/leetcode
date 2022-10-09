from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.lookup[key]

        left = 0
        right = len(candidates)
        while left < right:
            mid = left + (right - left) // 2
            prev_timestamp, _ = candidates[mid]
            if prev_timestamp <= timestamp:
                left = mid + 1
            else:
                right = mid

        return '' if right == 0 else candidates[right - 1][1]

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]

        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            prev_timestamp, _ = arr[mid]
            if prev_timestamp <= timestamp:
                left = mid + 1
            else:
                right = mid

        return '' if right == 0 else arr[right - 1][1]

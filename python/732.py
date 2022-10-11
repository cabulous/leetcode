from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def _update(self, start, end, left=0, right=10 ** 9, idx=1):
        if right < start or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = left + (right - left) // 2
            self._update(start, end, left, mid, idx * 2)
            self._update(start, end, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = self.lazy[idx] + max(self.vals[idx * 2], self.vals[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self._update(start, end - 1)
        return self.vals[1]

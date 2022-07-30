from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def _add(self, val: int):
        if len(self.queue) == self.size:
            self.queue.popleft()
        self.queue.append(val)

    def next(self, val: int) -> float:
        self._add(val)
        count = min(len(self.queue), self.size)
        return sum(self.queue) / count

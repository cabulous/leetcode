import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][idx][1]

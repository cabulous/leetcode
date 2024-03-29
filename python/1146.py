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
        snap_list = self.array[index]
        idx = bisect.bisect(snap_list, [snap_id + 1]) - 1
        return snap_list[idx][1]

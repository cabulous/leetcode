import bisect


# https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation
class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        sub_track = []
        if start % 2 == 0:
            sub_track.append(left)
        if end % 2 == 0:
            sub_track.append(right)

        self.track[start:end] = sub_track

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        sub_track = []
        if start % 2 == 1:
            sub_track.append(left)
        if end % 2 == 1:
            sub_track.append(right)

        self.track[start:end] = sub_track

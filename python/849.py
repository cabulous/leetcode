from itertools import groupby
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seat_count = len(seats)

        left = [seat_count] * seat_count
        for i in range(seat_count):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        right = [seat_count] * seat_count
        for i in range(seat_count - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < seat_count - 1:
                right[i] = right[i + 1] + 1

        dist = [min(left[i], right[i]) for i in range(seat_count) if seats[i] == 0]

        return max(dist)


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i, seat in enumerate(seats) if seat == 1)
        pre, nxt = None, next(people, None)
        res = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                pre = i
            else:
                while nxt is not None and nxt < i:
                    nxt = next(people, None)
                left = float('inf') if pre is None else i - pre
                right = float('inf') if nxt is None else nxt - i
                res = max(res, min(left, right))

        return res


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = seats.index(1)
        seats.reverse()
        res = max(res, seats.index(1))

        for seat, group in groupby(seats):
            if seat == 0:
                dist = len(list(group))
                res = max(res, (dist + 1) // 2)

        return res

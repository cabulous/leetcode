from itertools import groupby
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = len(seats)

        left = [count] * count
        for i in range(count):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        right = [count] * count
        for i in range(count - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < count - 1:
                right[i] = right[i + 1] + 1

        dist = [min(left[i], right[i]) for i in range(count) if seats[i] == 0]

        return max(dist)


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

import math


class Solution:

    def __init__(self):
        self.dist = []

    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        self.dist = dist

        left = 1
        hour_decimal = hour % 1 or 1
        right = math.ceil(max(dist) / hour_decimal)
        res = -1

        while left <= right:
            mid = left + (right - left) // 2
            time = self.get_time(mid)
            if time == hour:
                return mid
            if time < hour:
                right = mid - 1
                res = mid
            else:
                left = mid + 1

        return res

    def get_time(self, speed):
        res = sum(math.ceil(d / speed) for d in self.dist[:-1])
        res += self.dist[-1] / speed
        return res

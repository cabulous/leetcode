from collections import defaultdict
from typing import List


# https://leetcode.com/problems/max-points-on-a-line/discuss/47108/Python-68-ms-code/264385
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        point_count = len(points)
        res = 0

        for i in range(point_count):
            slopes = defaultdict(lambda: 1)
            same = 0
            x1, y1 = points[i]

            for j in range(i + 1, point_count):
                x2, y2 = points[j]
                dx, dy = x1 - x2, y1 - y2

                if dx == dy == 0:
                    same += 1
                    continue

                if dx == 0:
                    slope_key = 'vertical'
                else:
                    slope_key = self.frac(dx, dy)

                slopes[slope_key] += 1

            res = max(res, max(slopes.values() or [1]) + same)

        return res

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def frac(self, a, b):
        g = self.gcd(a, b)
        return a // g, b // g

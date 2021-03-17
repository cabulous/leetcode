import random
from typing import List


# https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/154092/Very-simple-Python-solution/636154
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        while True:
            a = random.uniform(-self.r, self.r)
            b = random.uniform(-self.r, self.r)
            if a ** 2 + b ** 2 <= self.r ** 2:
                return [a + self.xc, b + self.yc]

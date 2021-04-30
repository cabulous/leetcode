from math import log
from typing import List


# https://leetcode.com/problems/powerful-integers/discuss/214212/JavaC%2B%2BPython-Easy-Brute-Force
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs = {x ** i for i in range(20) if x ** i < bound}
        ys = {y ** i for i in range(20) if y ** i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))
        powerful_int = set()

        for i in range(a + 1):
            for j in range(b + 1):
                value = x ** i + y ** j
                if value <= bound:
                    powerful_int.add(value)
                if y == 1:
                    break
            if x == 1:
                break

        return list(powerful_int)

import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        bounces = p // math.gcd(p, q)
        if bounces % 2 == 1:
            if bounces * q // p % 2 == 1:
                return 1
            return 0
        return 2


# https://leetcode.com/problems/mirror-reflection/discuss/141773/C%2B%2BJavaPython-1-line-without-using-any-package-or
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        return 1 - p % 2 + q % 2

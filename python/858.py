import math


# https://leetcode.com/problems/mirror-reflection/discuss/938821/Python-pure-geometry-illustrated
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while k * q % p > 0:
            k += 1
        return 2 if k % 2 == 0 else (k * q // p) % 2


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        bounces = p // math.gcd(p, q)
        if bounces % 2 == 0:
            return 2
        if bounces * q // p % 2 == 1:
            return 1
        return 0

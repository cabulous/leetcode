import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and ((math.log(n) / math.log(2)) % 2) == 0


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1

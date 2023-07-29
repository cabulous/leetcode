class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            n = -n
            x = 1 / x

        res = 1.0
        cur = x
        while n > 0:
            if n % 2 == 1:
                res *= cur
            cur *= cur
            n >>= 1

        return res

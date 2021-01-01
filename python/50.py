class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        cur = x

        while n > 0:
            if n % 2 == 1:
                ans *= cur
            cur *= cur
            n >>= 1

        return ans

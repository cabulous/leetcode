class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7

        if n <= 2:
            return n

        f_prev, f_curr = 1, 2
        p_curr = 1

        for k in range(3, n + 1):
            tmp = f_curr
            f_curr = (f_curr + f_prev + 2 * p_curr) % mod
            p_curr = (p_curr + f_prev) % mod
            f_prev = tmp

        return f_curr

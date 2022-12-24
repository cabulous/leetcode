class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7

        if n <= 2:
            return n

        f_prev = 1
        f_curr = 2
        p_curr = 1

        for _ in range(3, n + 1):
            f_prev, f_curr, p_curr = f_curr, f_curr + f_prev + 2 * p_curr, p_curr + f_prev

        return f_curr % mod

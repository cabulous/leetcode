# https://leetcode.com/problems/nth-magical-number/discuss/154613/C%2B%2BJavaPython-Binary-Search

MOD = 10 ** 9 + 7


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        aa, bb = a, b

        while bb > 0:
            aa, bb = bb, aa % bb

        l, r, lcm = 2, 10 ** 14, a * b // aa

        while l < r:
            m = (l + r) // 2
            if m // a + m // b - m // lcm < n:
                l = m + 1
            else:
                r = m

        return l % MOD

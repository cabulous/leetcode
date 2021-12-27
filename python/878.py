# https://leetcode.com/problems/nth-magical-number/discuss/154613/C%2B%2BJavaPython-Binary-Search

MOD = 10 ** 9 + 7


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        aa, bb = a, b

        while bb > 0:
            aa, bb = bb, aa % bb

        left, right, lcm = 2, 10 ** 14, a * b // aa

        while left < right:
            mid = left + (right - left) // 2
            if mid // a + mid // b - mid // lcm < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD

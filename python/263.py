class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        dividend = n
        for factor in [2, 3, 5]:
            dividend = self.keep_dividing_when_divisible(dividend, factor)

        return dividend == 1

    def keep_dividing_when_divisible(self, dividend, divisor):
        while dividend % divisor == 0:
            dividend //= divisor
        return dividend

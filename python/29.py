class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while divisor >= dividend:
            power_of_two = -1
            value = divisor
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                power_of_two += power_of_two
            quotient += power_of_two
            dividend -= value

        return -quotient if negatives != 1 else quotient

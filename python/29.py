MAX_INT = 2147483647  # 2**31 - 1
MIN_INT = -2147483648  # -2**31
HALF_MIN_INT = -1073741824  # MIN_INT // 2


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        highest_double = divisor
        highest_power_of_two = -1
        while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
            highest_power_of_two += highest_power_of_two
            highest_double += highest_double

        quotient = 0
        while dividend <= divisor:
            if dividend <= highest_double:
                quotient += highest_power_of_two
                dividend -= highest_double
            highest_power_of_two >>= 1
            highest_double >>= 1

        return quotient if negatives == 1 else -quotient

import math


# four-square theorem and three-square theorem
# n=4^k(8m+7)
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        if self.is_square(n):
            return 1

        for base in range(1, int(math.sqrt(n)) + 1):
            if self.is_square(n - base ** 2):
                return 2

        return 3

    def is_square(self, n):
        return n == int(math.sqrt(n)) ** 2


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [0.0] + [float('inf')] * n

        for i in range(1, n + 1):
            for square_num in square_nums:
                if i < square_num:
                    break
                dp[i] = min(dp[i], 1 + dp[i - square_num])

        return int(dp[-1])

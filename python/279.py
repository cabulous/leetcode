import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [0.0] + [float('inf')] * n

        for i in range(1, n + 1):
            for square_num in square_nums:
                if i < square_num:
                    break
                dp[i] = min(dp[i], dp[i - square_num] + 1)

        return int(dp[-1])


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]

        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums
            for square_num in square_nums:
                if is_divided_by(n - square_num, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
        level = 0
        queue = {n}

        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    if remainder < square_num:
                        break
                    next_queue.add(remainder - square_num)
            queue = next_queue

        return level


class Solution:
    def numSquares(self, n: int) -> int:
        while n & 3 == 0:
            n >>= 2

        if n & 7 == 7:
            return 4

        if self.is_square(n):
            return 1

        for i in range(1, int(math.sqrt(n)) + 1):
            if self.is_square(n - i * i):
                return 2

        return 3

    def is_square(self, n):
        return n == int(math.sqrt(n)) ** 2

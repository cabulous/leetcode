from collections import defaultdict


class Solution:
    def fib(self, n: int) -> int:
        m = defaultdict(int)

        def helper(n):
            if n <= 1:
                return n
            if n == 2:
                return 1
            if not m[n]:
                m[n] = helper(n - 1) + helper(n - 2)
            return m[n]

        return helper(n)


# Iterative Top-Down Approach
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        curr = 0
        prev1 = prev2 = 1

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = curr, prev1

        return curr


# Matrix Exponentiation
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        a = [[1, 1], [1, 0]]
        self.matrix_power(a, n - 1)
        return a[0][0]

    def matrix_power(self, a, n):
        if n <= 1:
            return a
        self.matrix_power(a, n // 2)
        self.multiply(a, a)
        b = [[1, 1], [1, 0]]
        if n % 2 != 0:
            self.multiply(a, b)

    def multiply(self, a, b):
        x = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        y = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        z = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        w = a[1][0] * b[0][1] + a[1][1] * b[1][1]

        a[0][0] = x
        a[0][1] = y
        a[1][0] = z
        a[1][1] = w


# Math
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)

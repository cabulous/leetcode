# Recursion with memoization - forward
class Solution:
    def climbStairs(self, n):
        memo = {}

        def helper(cur):
            if cur > n:
                return 0
            if cur == 1 or cur == 2:
                return cur
            if cur in memo:
                return memo[cur]
            memo[cur] = helper(cur - 1) + helper(cur - 2)
            return memo[cur]

        return helper(n)


# Dynamic programming
class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n

        pre, cur = 1, 2

        for _ in range(3, n + 1):
            pre, cur = cur, pre + cur

        return cur


# Binets Method
class Solution:
    def climbStairs(self, n):
        def multiply(a, b):
            c = [[0] * 2 for _ in range(2)]
            for i in range(2):
                for j in range(2):
                    c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            return c

        def powMatrix(a, n):
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1 == 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        q = [[1, 1], [1, 0]]
        res = powMatrix(q, n)
        return res[0][0]

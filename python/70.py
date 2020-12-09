# Recursion with memoization - forward
class Solution:
    def climbStairs(self, n):
        def helper(cur=0):
            if cur > n:
                return 0
            if cur == n:
                return 1
            if memo[cur] > 0:
                return memo[cur]
            memo[cur] = helper(cur + 1) + helper(cur + 2)
            return memo[cur]

        memo = [0] * (n + 1)
        return helper()


# Recursion with memoization - backward
class Solution:
    def climbStairs(self, n):
        def helper(cur=n):
            if cur <= 0:
                return 0
            if cur == 1:
                return 1
            if cur == 2:
                return 2
            if memo[cur] > 0:
                return memo[cur]
            memo[cur] = helper(cur - 1) + helper(cur - 2)
            return memo[cur]

        memo = [0] * (n + 1)
        return helper()


# Dynamic programming
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


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

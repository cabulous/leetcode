class Solution:

    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):
        return self.helper(n)

    def helper(self, n):
        if n <= 2:
            return n

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.helper(n - 1) + self.helper(n - 2)

        return self.memo[n]


class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        pre, cur = 1, 2
        for _ in range(3, n + 1):
            pre, cur = cur, pre + cur

        return cur

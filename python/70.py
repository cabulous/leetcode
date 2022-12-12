class Solution:

    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):
        return self.helper(n)

    def helper(self, curr):
        if curr <= 2:
            return curr

        if curr in self.memo:
            return self.memo[curr]

        self.memo[curr] = self.helper(curr - 1) + self.helper(curr - 2)

        return self.memo[curr]


class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        pre, cur = 1, 2

        for _ in range(3, n + 1):
            pre, cur = cur, pre + cur

        return cur

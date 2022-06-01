class Solution:

    def __init__(self):
        self.memo = {}

    def minKnightMoves(self, x: int, y: int) -> int:
        return self.dfs(abs(x), abs(y))

    def dfs(self, x, y):
        if x == y == 0:
            return 0

        if x + y == 2:
            return 2

        if (x, y) in self.memo:
            return self.memo[x, y]

        self.memo[x, y] = 1 + min(
            self.dfs(abs(x - 1), abs(y - 2)),
            self.dfs(abs(x - 2), abs(y - 1)),
        )

        return self.memo[x, y]

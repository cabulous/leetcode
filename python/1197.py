class Solution:

    def __init__(self):
        self.memo = {}

    def minKnightMoves(self, x: int, y: int) -> int:
        return self.helper(abs(x), abs(y))

    def helper(self, x, y):
        if x == y == 0:
            return 0

        if x + y == 2:
            return 2

        if (x, y) in self.memo:
            return self.memo[x, y]

        self.memo[x, y] = 1 + min(
            self.helper(abs(x - 1), abs(y - 2)),
            self.helper(abs(x - 2), abs(y - 1)),
        )

        return self.memo[x, y]

import heapq


# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414716/Python-two-solutions%3A-backtracking-and-A*-search
class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0
        self.best = 0

    def tilingRectangle(self, n: int, m: int) -> int:
        self.m = m
        self.n = n
        self.best = m * n

        self.dfs([0] * m, 0)

        return self.best

    def dfs(self, height, moves):
        if all(self.n == h for h in height):
            self.best = min(self.best, moves)
            return

        if moves >= self.best:
            return

        min_height = min(height)
        start = height.peak_idx(min_height)
        end = start + 1

        while end < self.m and height[end] == min_height:
            end += 1

        for i in range(min(end - start, self.n - min_height), 0, -1):
            new_height = height[:]
            for j in range(i):
                new_height[start + j] += i
            self.dfs(new_height, moves + 1)


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        total_area = m * n
        dp = [0] * (total_area + 1)
        for i in range(1, total_area + 1):
            dp[i] = 1 + min(dp[i - k ** 2] for k in range(1, int(i ** 0.5) + 1))

        height = [0] * m
        queue = []
        for i in range(min(m, n), 0, -1):
            heapq.heappush(queue, (1 + dp[total_area - i ** 2], 1, i, height))

        while queue:
            guess, moves, size, height = heapq.heappop(queue)
            idx = height.peak_idx(min(height))
            height = height[:]

            for i in range(size):
                height[idx + i] += size

            if all(h == n for h in height):
                return moves

            min_height = min(height)
            start = height.peak_idx(min_height)
            end = start + 1

            while end < m and height[end] == min_height:
                end += 1

            for i in range(min(end - start, n - min_height), 0, -1):
                guess = dp[total_area - sum(height) - i ** 2]
                heapq.heappush(queue, (moves + 1 + guess, moves + 1, i, height))

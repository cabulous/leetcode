class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            next_dp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            next_dp[nr][nc] += dp[r][c] / 8.0
            dp = next_dp

        return sum(sum(row) for row in dp)

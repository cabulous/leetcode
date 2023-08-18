class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        in_degrees = [0] * n
        is_connected = [[False] * n for _ in range(n)]

        for u, v in roads:
            in_degrees[u] += 1
            in_degrees[v] += 1
            is_connected[u][v] = is_connected[v][u] = True

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                curr = in_degrees[i] + in_degrees[j]
                if is_connected[i][j]:
                    curr -= 1
                res = max(res, curr)

        return res

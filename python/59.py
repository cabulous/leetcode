# Layer
class Solution:
    def generateMatrix(self, n):
        res = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        for layer in range((n + 1) // 2):
            for ptr in range(layer, n - layer):
                res[layer][ptr] = count
                count += 1
            for ptr in range(layer + 1, n - layer):
                res[ptr][n - layer - 1] = count
                count += 1
            for ptr in range(layer + 1, n - layer):
                res[n - layer - 1][n - ptr - 1] = count
                count += 1
            for ptr in range(layer + 1, n - layer - 1):
                res[n - ptr - 1][layer] = count
                count += 1
        return res


# Walk the spiral
class Solution:
    def generateMatrix(self, n):
        res = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for k in range(n * n):
            res[x][y] = k + 1
            if res[(x + dx) % n][(y + dy) % n]:
                dx, dy = dy, -dx
            x += dx
            y += dy
        return res


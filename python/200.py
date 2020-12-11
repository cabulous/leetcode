# DFS
class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.grid = []
        self.max_x = 0
        self.max_y = 0
        self.visited = set()

    def numIslands(self, grid: [[str]]) -> int:
        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        return sum([self.floodfill_dfs(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_dfs(self, x, y):
        if not self.is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodfill_dfs(x + self.dx[k], y + self.dy[k])
        return 1

    def is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True


# BFS
from collections import deque


class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.grid = []
        self.max_x = 0
        self.max_y = 0
        self.visited = set()

    def numIslands(self, grid: [[str]]) -> int:
        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        return sum([self.floodfill_bfs(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_bfs(self, x, y):
        if not self.is_valid(x, y):
            return 0
        self.visited.add((x, y))
        queue = deque()
        queue.append((x, y))
        while queue:
            cx, cy = queue.popleft()
            for k in range(4):
                nx, ny = cx + self.dx[k], cy + self.dy[k]
                if self.is_valid(nx, ny):
                    self.visited.add((nx, ny))
                    queue.append((nx, ny))
        return 1

    def is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True


# Union Find
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0

        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for k in range(4):
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                            uf.union(i * n + j, ni * n + nj)

        return uf.count

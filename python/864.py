# https://leetcode.com/problems/shortest-path-to-get-all-keys/discuss/364604/Python-Level-by-level-BFS-Solution-(292-ms-beat-97.78)-(similar-problems-listed)
class Solution:

    def __init__(self):
        self.grid = []

    def shortestPathAllKeys(self, grid: list[str]) -> int:
        self.grid = grid

        rows = len(grid)
        cols = len(grid[0])
        start = []
        all_keys = [0] * 6
        for r in range(rows):
            for c in range(cols):
                if self.is_start(r, c):
                    start = r, c
                elif self.is_key(r, c):
                    all_keys[self.hash_key(r, c)] = 1
        all_keys = tuple(all_keys)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(start[0], start[1], tuple([0] * 6))]
        visited = {(start[0], start[1], tuple([0] * 6))}
        res = 0

        while queue:
            next_queue = []
            for r, c, keys in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or rows <= nr or nc < 0 or cols <= nc:
                        continue
                    elif self.is_wall(nr, nc):
                        continue
                    elif self.is_empty(nr, nc):
                        if (nr, nc, keys) not in visited:
                            visited.add((nr, nc, keys))
                            next_queue.append((nr, nc, keys))
                    elif self.is_key(nr, nc):
                        nk = list(keys)
                        nk[self.hash_key(nr, nc)] = 1
                        nk = tuple(nk)
                        if nk == all_keys:
                            return res + 1
                        if (nr, nc, nk) not in visited:
                            visited.add((nr, nc, nk))
                            next_queue.append((nr, nc, nk))
                    elif self.is_lock(nr, nc):
                        if self.has_key_for_lock(nr, nc, keys) and (nr, nc, keys) not in visited:
                            visited.add((nr, nc, keys))
                            next_queue.append((nr, nc, keys))
            queue = next_queue
            res += 1

        return -1

    def is_start(self, row, col):
        return self.grid[row][col] == '@'

    def is_key(self, row, col):
        return self.grid[row][col].islower()

    def hash_key(self, row, col):
        return ord(self.grid[row][col].lower()) - ord('a')

    def is_wall(self, row, col):
        return self.grid[row][col] == '#'

    def is_empty(self, row, col):
        return self.grid[row][col] == '.' or self.is_start(row, col)

    def is_lock(self, row, col):
        return self.grid[row][col].isupper()

    def has_key_for_lock(self, row, col, keys):
        return keys[self.hash_key(row, col)] == 1

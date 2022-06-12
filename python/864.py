from typing import List


# https://leetcode.com/problems/shortest-path-to-get-all-keys/discuss/364604/Python-Level-by-level-BFS-Solution-(292-ms-beat-97.78)-(similar-problems-listed)
class Solution:

    def __init__(self):
        self.grid = []

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not any(grid):
            return -1

        self.grid = grid
        rows = len(grid)
        cols = len(grid[0])
        all_keys = [0, 0, 0, 0, 0, 0]
        start = []

        for row in range(rows):
            for col in range(cols):
                if self.is_start(row, col):
                    start = row, col
                elif self.is_key(row, col):
                    all_keys[self.hash_key(row, col)] = 1

        all_keys = tuple(all_keys)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_level = [(start[0], start[1], tuple([0] * 6))]
        visited = {(start[0], start[1], tuple([0] * 6))}
        moves = 0

        while curr_level:
            next_level = []

            for r, c, keys in curr_level:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not self.is_wall(nr, nc):
                        if self.is_empty(nr, nc):
                            if (nr, nc, keys) not in visited:
                                visited.add((nr, nc, keys))
                                next_level.append((nr, nc, keys))
                        elif self.is_key(nr, nc):
                            new_keys = list(keys)
                            new_keys[self.hash_key(nr, nc)] = 1
                            new_keys = tuple(new_keys)
                            if new_keys == all_keys:
                                return moves + 1
                            if (nr, nc, new_keys) not in visited:
                                visited.add((nr, nc, new_keys))
                                next_level.append((nr, nc, new_keys))
                        elif self.is_lock(nr, nc):
                            if keys[self.hash_key(nr, nc)] == 1 and (nr, nc, keys) not in visited:
                                visited.add((nr, nc, keys))
                                next_level.append((nr, nc, keys))

            curr_level = next_level
            moves += 1

        return -1

    def is_start(self, row, col):
        return self.grid[row][col] == '@'

    def hash_key(self, row, col):
        return ord(self.grid[row][col].lower()) - ord('a')

    def is_key(self, row, col):
        return self.grid[row][col].islower()

    def is_lock(self, row, col):
        return self.grid[row][col].isupper()

    def is_wall(self, row, col):
        return self.grid[row][col] == '#'

    def is_empty(self, row, col):
        return self.grid[row][col] == '.' or self.is_start(row, col)

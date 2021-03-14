from typing import List


# Hash By Path Signature
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row_max, col_max = len(grid), len(grid[0])
        seen = set()
        unique_islands = set()

        def dfs(row, col, direction):
            if row < 0 or row >= row_max or col < 0 or col >= col_max:
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            path_signature.append(direction)
            dfs(row + 1, col, 'D')
            dfs(row - 1, col, 'U')
            dfs(row, col + 1, 'R')
            dfs(row, col - 1, 'L')
            path_signature.append('0')

        for row in range(row_max):
            for col in range(col_max):
                path_signature = []
                dfs(row, col, '0')
                if path_signature:
                    unique_islands.add(tuple(path_signature))

        return len(unique_islands)


#  Hash By Local Coordinates
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row_max, col_max = len(grid), len(grid[0])
        seen = set()
        unique_islands = set()

        def dfs(row, col):
            if row < 0 or row >= row_max or col < 0 or col >= col_max:
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(row_max):
            for col in range(col_max):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if current_island:
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)

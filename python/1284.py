from collections import deque
from typing import List


# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/discuss/446342/JavaPython-3-Convert-matrix-to-int%3A-BFS-and-DFS-codes-w-explanation-comments-and-analysis.
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        start = sum(cell << (r * cols + c) for r, row in enumerate(mat) for c, cell in enumerate(row))
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            curr, step = queue.popleft()
            if curr == 0:
                return step
            for r in range(rows):
                for c in range(cols):
                    nxt = curr
                    for nr, nc in (r, c), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                        if 0 <= nr < rows and 0 <= nc < cols:
                            nxt ^= 1 << (nr * cols + nc)
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, step + 1))

        return -1

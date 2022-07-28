from typing import List


# https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107396/Python-solution-based-on-wufangjie's-(Hadlock's-algorithm)
class Solution:

    def __init__(self):
        self.forest = []

    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.forest = forest

        self.forest.append([0] * len(self.forest[0]))
        for row in self.forest:
            row.append(0)

        trees = [
            (height, i, j)
            for i, row in enumerate(self.forest)
            for j, height in enumerate(row)
            if height > 1
        ]

        queue = [(0, 0)]
        seen = set()
        for r, c in queue:
            if (r, c) not in seen and self.forest[r][c] > 0:
                seen.add((r, c))
                queue += (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)

        if not all((r, c) in seen for (_, r, c) in trees):
            return -1

        trees.sort()

        return sum(self.distance(sr, sc, er, ec) for (_, sr, sc), (_, er, ec) in zip([(0, 0, 0)] + trees, trees))

    def distance(self, start_r, start_c, end_r, end_c):
        now = [(start_r, start_c)]
        soon = []
        expanded = set()
        manhattan = abs(start_r - end_r) + abs(start_c - end_c)
        detours = 0

        while True:
            if not now:
                now, soon = soon, []
                detours += 1

            r, c = now.pop()
            if (r, c) == (end_r, end_c):
                return manhattan + 2 * detours

            if (r, c) not in expanded:
                expanded.add((r, c))
                for nr, nc, closer in (r + 1, c, r < end_r), (r - 1, c, r > end_r), (r, c + 1, c < end_c), (r, c - 1, c > end_c):
                    if self.forest[nr][nc] > 0:
                        (now if closer else soon).append((nr, nc))

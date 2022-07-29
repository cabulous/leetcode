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
            (height, r, c)
            for r, row in enumerate(self.forest)
            for c, height in enumerate(row)
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

        return sum(
            self.distance(start_row, start_col, end_row, end_col)
            for (_, start_row, start_col), (_, end_row, end_col)
            in zip([(0, 0, 0)] + trees, trees)
        )

    def distance(self, start_row, start_col, end_row, end_col):
        now = [(start_row, start_col)]
        soon = []
        expanded = set()
        curr_dist = abs(start_row - end_row) + abs(start_col - end_col)
        detours = 0

        while True:
            if not now:
                now, soon = soon, []
                detours += 1

            curr_row, curr_col = now.pop()
            if (curr_row, curr_col) == (end_row, end_col):
                return curr_dist + 2 * detours

            if (curr_row, curr_col) not in expanded:
                expanded.add((curr_row, curr_col))

                next_steps = [
                    (curr_row + 1, curr_col, curr_row < end_row),
                    (curr_row - 1, curr_col, curr_row > end_row),
                    (curr_row, curr_col + 1, curr_col < end_col),
                    (curr_row, curr_col - 1, curr_col > end_col),
                ]

                for next_row, next_col, closer in next_steps:
                    if self.forest[next_row][next_col] > 0:
                        (now if closer else soon).append((next_row, next_col))

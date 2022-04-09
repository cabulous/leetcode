from collections import Counter
from itertools import chain, product
from typing import List


# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/discuss/1549108/Python-short-solution-explained
class Solution:

    def __init__(self):
        self.res = set()

    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        positions = [tuple(x) for x in positions]
        poss = {
            'rook': ((1, 0), (-1, 0), (0, 1), (0, -1)),
            'bishop': ((1, 1), (1, -1), (-1, 1), (-1, -1)),
            'queen': ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)),
        }

        for dirs in product(*(poss[i] for i in pieces)):
            self.dfs(positions, dirs, (1 << len(pieces)) - 1)

        return len(self.res)

    def dfs(self, pos, dirs, stopped_mask):
        if stopped_mask == 0:
            return

        self.res.add(tuple(pos))

        for active in range(1 << len(dirs)):
            if (stopped_mask & active) != active:
                continue

            new_pos = list(pos)
            new_mask = stopped_mask ^ active

            for i in range(len(new_pos)):
                new_pos[i] = (
                    new_pos[i][0] + dirs[i][0] * ((new_mask >> i) & 1),
                    new_pos[i][1] + dirs[i][1] * ((new_mask >> i) & 1)
                )

            if len(Counter(new_pos)) < len(dirs):
                continue

            all_c = list(chain(*new_pos))

            if min(all_c) <= 0 or max(all_c) > 8:
                continue

            self.dfs(new_pos, dirs, new_mask)

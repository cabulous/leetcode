from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.sticks = []
        self.side_target = 0

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        self.side_target, rem = divmod(sum(matchsticks), 4)
        if rem != 0:
            return False

        self.sticks = sorted(matchsticks, reverse=True)

        return self.helper(0, (0, 0, 0, 0))

    @lru_cache(None)
    def helper(self, stick_idx, sides):
        if stick_idx == len(self.sticks):
            return sides[0] == sides[1] == sides[2] == self.side_target

        for i in range(4):
            if sides[i] + self.sticks[stick_idx] <= self.side_target:
                next_sides = list(sides)
                next_sides[i] += self.sticks[stick_idx]
                if self.helper(stick_idx + 1, tuple(next_sides)):
                    return True

        return False

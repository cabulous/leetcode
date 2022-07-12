from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.sticks = []
        self.side_target = 0

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        perimeter = sum(matchsticks)
        self.side_target = perimeter // 4

        if self.side_target * 4 != perimeter:
            return False

        self.sticks = sorted(matchsticks, reverse=True)

        return self.helper(0, (0, 0, 0, 0))

    @lru_cache(None)
    def helper(self, index, sides):
        if index == len(self.sticks):
            return sides[0] == sides[1] == sides[2] == self.side_target

        for i in range(4):
            if sides[i] + self.sticks[index] <= self.side_target:
                new_sides = list(sides)
                new_sides[i] += self.sticks[index]
                new_sides = tuple(new_sides)
                if self.helper(index + 1, new_sides):
                    return True

        return False

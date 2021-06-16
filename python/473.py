from functools import lru_cache
from typing import List


# dfs
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        basket, rem = divmod(sum(matchsticks), 4)
        if rem:
            return False

        sticks = sorted(matchsticks, reverse=True)
        sides = [0, 0, 0, 0]

        def dfs(index):
            if index == len(sticks):
                return sides[0] == sides[1] == sides[2] == basket
            for i in range(4):
                if sides[i] + sticks[index] <= basket:
                    sides[i] += sticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= sticks[index]
            return False

        return dfs(0)


# dp
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        side = perimeter // 4

        if side * 4 != perimeter:
            return False

        memo = {}

        def recurse(mask, sides_done):
            total = 0

            for i in range(n - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[n - 1 - i]

            if total > 0 and total % side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            ans = False
            c = int(total / side)
            rem = side * (c + 1) - total

            for i in range(n - 1, -1, -1):
                if matchsticks[n - 1 - i] <= rem and mask & (1 << i):
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break

            memo[(mask, sides_done)] = ans

            return ans

        return recurse((1 << n) - 1, 0)


# https://leetcode.com/problems/matchsticks-to-square/discuss/1273708/Python-dp-on-subsets-explained
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        basket, rem = divmod(sum(matchsticks), 4)
        if rem or max(matchsticks) > basket:
            return False

        @lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            for j in range(n):
                if mask & 1 << j:
                    nei = dfs(mask ^ (1 << j))
                    if nei >= 0 and nei + matchsticks[j] <= basket:
                        return (nei + matchsticks[j]) % basket
            return -1

        return dfs((1 << n) - 1) == 0

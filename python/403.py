from typing import List


# https://leetcode.com/problems/frog-jump/discuss/88800/Python-Documented-solution-that-is-easy-to-understand/93592
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        d = {stone: set() for stone in stones}
        d[1].add(1)

        for stone in stones[:-1]:
            for last_jump in d[stone]:
                for jump in range(last_jump - 1, last_jump + 2):
                    if jump > 0 and (stone + jump) in d:
                        d[stone + jump].add(jump)

        return bool(d[stones[-1]])

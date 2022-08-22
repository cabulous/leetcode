from functools import lru_cache

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
class Solution:

    def __init__(self):
        self.k = 0

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.k = k
        return self.helper(n, target)

    @lru_cache(None)
    def helper(self, dice_remain, target):
        if dice_remain == 0:
            return 1 if target == 0 else 0

        res = 0
        for i in range(1, self.k + 1):
            res += self.helper(dice_remain - 1, target - i)

        return res % MOD

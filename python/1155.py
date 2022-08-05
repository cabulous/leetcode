MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
class Solution:

    def __init__(self):
        self.k = 0
        self.memo = {}

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.k = k
        return self.helper(n, target)

    def helper(self, dice_remain, target):
        if dice_remain == 0:
            return 1 if target == 0 else 0

        if (dice_remain, target) in self.memo:
            return self.memo[dice_remain, target]

        res = 0
        for next_target in range(max(0, target - self.k), target):
            res += self.helper(dice_remain - 1, next_target)

        self.memo[dice_remain, target] = res % MOD

        return self.memo[dice_remain, target]

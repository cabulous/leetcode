MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
class Solution:

    def __init__(self):
        self.k = 0
        self.memo = {}

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.k = k
        return self.dp(n, target) % MOD

    def dp(self, dice_count, target):
        if dice_count == 0:
            return 0 if target > 0 else 1

        if (dice_count, target) in self.memo:
            return self.memo[dice_count, target]

        res = 0
        for next_target in range(max(0, target - self.k), target):
            res += self.dp(dice_count - 1, next_target)

        self.memo[dice_count, target] = res

        return res

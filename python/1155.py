MOD = 10 ** 9 + 7


class Solution:

    def __init__(self):
        self.memo = {}
        self.k = 0

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.k = k
        return self.dp(n, target) % MOD

    def dp(self, dice_remain, target_remain):
        if dice_remain == 0:
            return 0 if target_remain > 0 else 1

        if (dice_remain, target_remain) in self.memo:
            return self.memo[dice_remain, target_remain]

        res = 0
        for k in range(max(0, target_remain - self.k), target_remain):
            res += self.dp(dice_remain - 1, k)

        self.memo[dice_remain, target_remain] = res

        return res

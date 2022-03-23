class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0

        while target > startValue:
            res += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2

        return res + startValue - target

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y > X:
            ans += 1
            if Y & 1 == 1:
                Y += 1
            else:
                Y >>= 1
        return ans + X - Y

# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/solutions/477690/java-python-3-bit-manipulation-w-explanation-and-analysis/
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        diff = (a | b) ^ c
        res = 0

        for i in range(31):
            mask = 1 << i
            if mask & diff > 0:
                if (a & mask) == (b & mask) and c & mask == 0:
                    res += 2
                else:
                    res += 1

        return res

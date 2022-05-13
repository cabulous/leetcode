import math


# https://leetcode.com/problems/smallest-good-base/discuss/96587/Python-solution-with-detailed-mathematical-explanation-and-derivation
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        max_m = int(math.log(num, 2))

        for m in range(max_m, 1, -1):
            k = int(num ** m ** -1)
            if (k ** (m + 1) - 1) // (k - 1) == num:
                return str(k)

        return str(num - 1)

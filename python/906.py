# https://leetcode.com/problems/super-palindromes/discuss/170742/Python-super-easy-to-understand-105-complexity-no-cheating
import math


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l, r = int(left), int(right)
        sqrtl, sqrtr = int(math.sqrt(l)), int(math.sqrt(r))
        n1, n2 = len(str(sqrtl)), len(str(sqrtr))

        n1 = n1 // 2 if n1 & 1 == 0 else n1 // 2 + 1
        n2 = n2 // 2 if n2 & 1 == 0 else n2 // 2 + 1

        start = int('1' + '0' * (n1 - 1))
        end = int('9' * n2) + 1
        ans = 0

        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])
            num2 = int(x[:-1] + x[::-1])
            for num in [num1, num2]:
                candidate = num * num
                if l <= candidate <= r and str(candidate) == str(candidate)[::-1]:
                    ans += 1

        return ans

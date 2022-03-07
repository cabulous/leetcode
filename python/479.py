# https://leetcode.com/problems/largest-palindrome-product/discuss/171580/Python-Solution-using-Math-and-Detailed-Mathematical-deduction
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        for z in range(2, 2 * (9 * 10 ** n) - 1):
            left = 10 ** n - z
            right = int(str(left)[::-1])

            if z ** 2 - 4 * right < 0:
                continue
            else:
                root_1 = 1 / 2 * (z + (z ** 2 - 4 * right) ** 0.5)
                root_2 = 1 / 2 * (z - (z ** 2 - 4 * right) ** 0.5)
                if root_1.is_integer() or root_2.is_integer():
                    return (10 ** n * left + right) % 1337

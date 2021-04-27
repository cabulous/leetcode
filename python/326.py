class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


# any prime number
# https://leetcode.com/problems/power-of-three/discuss/77977/Math-1-liner-no-log-with-explanation
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

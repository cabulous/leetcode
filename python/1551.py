# Math
class Solution:
    def minOperations(self, n: int) -> int:
        return n ** 2 // 4 if n % 2 == 0 else (n ** 2 - 1) // 4


# Brute Force
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n - 1
            n -= 2
        return res

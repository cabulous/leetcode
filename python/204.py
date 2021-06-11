import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        non_prime_nums = {}

        for num in range(2, int(math.sqrt(n)) + 1):
            if num not in non_prime_nums:
                for multiple in range(num * num, n, num):
                    non_prime_nums[multiple] = 1

        return n - len(non_prime_nums) - 2

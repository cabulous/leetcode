from math import ceil


# N = x k + k(k + 1)/2
# x > 0 --> N/k - (k + 1)/2 > 0
# k < (2n + 0.25)**0.5 - 0.5
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upper_limit = ceil((2 * n + 0.25) ** 0.5 - 0.5) + 1

        for k in range(1, upper_limit):
            n -= k
            if n % k == 0:
                count += 1

        return count

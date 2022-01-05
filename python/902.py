from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_length = len(n_str)
        dp = [0] * n_length + [1]

        for i in reversed(range(n_length)):
            for d in digits:
                if d < n_str[i]:
                    dp[i] += len(digits) ** (n_length - i - 1)
                elif d == n_str[i]:
                    dp[i] += dp[i + 1]

        return dp[0] + sum(len(digits) ** i for i in range(1, n_length))

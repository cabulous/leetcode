from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        dp = [0] * len(arr)

        for curr in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[curr]:
                stack.pop()
            if stack:
                prev = stack[-1]
                dp[curr] = dp[prev] + (curr - prev) * arr[curr]
            else:
                dp[curr] = (curr + 1) * arr[curr]
            stack.append(curr)

        return sum(dp) % MOD

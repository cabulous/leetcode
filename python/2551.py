# https://leetcode.com/problems/put-marbles-in-bags/solutions/3111736/java-c-python-3-approachs-best-o-n/
class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        total = []
        for i in range(len(weights) - 1):
            total.append(weights[i] + weights[i + 1])

        total.sort()

        res = 0
        for i in range(k - 1):
            res += total[len(total) - 1 - i] - total[i]

        return res

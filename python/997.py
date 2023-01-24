from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        trust_count = [0] * (n + 1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1

        for i, count in enumerate(trust_count[1:], 1):
            if count == n - 1:
                return i

        return -1

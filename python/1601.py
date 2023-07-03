from collections import Counter

from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        for i in range(len(requests) - 1, -1, -1):
            for comb in combinations(requests, i + 1):
                source = Counter(s for s, t in comb)
                target = Counter(t for s, t in comb)
                if source == target:
                    return i + 1
        return 0

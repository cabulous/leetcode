from collections import Counter

from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        for i in range(len(requests), 0, -1):
            for comb in combinations(requests, i):
                source = Counter(s for s, t in comb)
                target = Counter(t for s, t in comb)
                if source == target:
                    return i
        return 0

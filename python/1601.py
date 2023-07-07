from collections import Counter

from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        for count in range(len(requests), 0, -1):
            for comb in combinations(requests, count):
                source = Counter(s for s, t in comb)
                target = Counter(t for s, t in comb)
                if source == target:
                    return count
        return 0

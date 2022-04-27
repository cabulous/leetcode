from collections import defaultdict
from typing import List


# https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation
class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)

        m = defaultdict(list)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())

        return ''.join(res)

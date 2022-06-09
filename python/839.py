from typing import List


# https://leetcode.com/problems/similar-string-groups/discuss/132317/Simple-Java-8-Python-Union-Find
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
            self.parent[root_x] = root_y


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                diff = sum(strs[i][k] != strs[j][k] for k in range(len(strs[i])))
                if diff in (0, 2):
                    uf.union(i, j)

        res = set(uf.find(i) for i in range(n))

        return len(res)

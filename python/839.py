from typing import List


# https://leetcode.com/problems/similar-string-groups/discuss/132317/Simple-Java-8-Python-Union-Find
class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(len(strs))

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                str1 = strs[i]
                str2 = strs[j]
                diff = sum(str1[k] != str2[k] for k in range(len(str1)))
                if diff in (0, 2):
                    uf.union(i, j)

        res = set(uf.find(i) for i in range(len(strs)))

        return len(res)

from typing import List
from collections import defaultdict


# https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/909142/Python-Union-Find
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i, j])

        for val in sorted(d):
            p = [i for i in range(m + n)]
            rank2 = rank[:]
            for i, j in d[val]:
                i, j = self.find(p, i), self.find(p, j + n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[val]:
                rank[i] = rank[j + n] = matrix[i][j] = rank2[self.find(p, i)] + 1

        return matrix

    def find(self, p, i):
        if p[i] != i:
            p[i] = self.find(p, p[i])
        return p[i]

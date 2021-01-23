from heapq import heappush, heappop
from typing import List
from collections import defaultdict


# hashmap of heaps
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        h = defaultdict(list)

        for i in range(n):
            for j in range(m):
                heappush(h[i - j], mat[i][j])

        for i in range(n):
            for j in range(m):
                mat[i][j] = heappop(h[i - j])

        return mat


# space O(min(m ,n))
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        def sort_diagonal(i, j):
            diagonal = []
            while i < n and j < m:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = diagonal.pop()

        for i in range(n):
            sort_diagonal(i, 0)
        for j in range(m):
            sort_diagonal(0, j)

        return mat

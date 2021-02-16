import itertools
from typing import List
import heapq


# Vertical Iteration
# O(m * n)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        indexes = []
        for c, r in itertools.product(range(n), range(m)):
            if len(indexes) == k:
                break
            if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
                indexes.append(r)

        # If there aren't enough, it's because some of the first k weakest rows are entirely 1's.
        i = 0
        while len(indexes) < k:
            if mat[i][-1] == 1:
                indexes.append(i)
            i += 1

        return indexes


# Binary Search and Priority Queue
# O(m log nk)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        def binary_search(row):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        q = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(q) < k or entry > q[0]:
                heapq.heappush(q, entry)
            if len(q) > k:
                heapq.heappop(q)

        indexes = []
        while q:
            _, i = heapq.heappop(q)
            indexes.append(-i)
        indexes = indexes[::-1]

        return indexes


# Binary Search and Sorting/ Map
# O(m log mn)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])

        def binary_search(row):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        strengths = [(binary_search(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [i for _, i in strengths[:k]]


# linear search and sorting
# O(m * n + m log m)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [i for _, i in strengths[:k]]
